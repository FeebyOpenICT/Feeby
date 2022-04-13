from typing import Optional
from fastapi import APIRouter, Cookie, Depends, Response, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
import requests

from Exceptions.AuthenticationException import OAuth2AuthenticationException
from Exceptions.NotFound import NotFound
from Repositories.RoleRepository import RoleRepository
from Repositories.UserRepository import UserRepository
from .JWTToken import AccessToken
from Auth.validate_user import token_auth_scheme
from database import get_db_connection
from config import BASE_URL, DELEVOPER_KEY_ID, DEVELOPER_KEY, BASE_APP_API_CALLBACK_URL
from Models.UserModel import UserModel
from Models.RoleModel import RoleModel
from Schemas.RolesEnum import RolesEnum

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.get("/callback")
async def callback(response: Response, jwt: Optional[str] = Cookie(None), code: str = None, error: str = None, error_description: str = None, db: Session = Depends(get_db_connection)):
    """
    Callback for oauth2 flow https://canvas.instructure.com/doc/api/file.oauth.html
    """
    if error:
        # Something went wrong or the user denied access
        if error_description:
            raise OAuth2AuthenticationException(message=error_description)
        raise OAuth2AuthenticationException(title=error)
    elif code:
        # TODO verify state
        r = requests.post(f'{BASE_URL}/login/oauth2/token', data={
            'grant_type': 'authorization_code',
            'client_id': DELEVOPER_KEY_ID,
            'client_secret': DEVELOPER_KEY,
            'redirect_uri': BASE_APP_API_CALLBACK_URL,
            'code': code
        })
        # got the access_token, now check for errors:
        if r.status_code >= 400:
            if r.status_code == 500:
                # Canceled oauth or server error
                raise OAuth2AuthenticationException(
                    status_code=500, message="An error occured on the canvas authentication servers. Please refresh the page and try again. Contact support if the issue persists.")
            else:
                raise OAuth2AuthenticationException(status_code=r.status_code)

        json = r.json()

        """ json ^
        {
            "access_token": str,
            "token_type": "Bearer",
            "user": {
                "id": int, 
                "name": str
            },
            "refresh_token": str,
            "expires_in": int
        }
        """

        # check if user already exists in db
        jwt_token = AccessToken.decode_token(jwt)

        if jwt_token.canvas_id != json["user"]["id"]:
            raise OAuth2AuthenticationException(
                message=f"LTI launch user_id: {jwt_token.canvas_id}, type: {type(jwt_token.canvas_id).__name__} does not equal get token user_id: {json['user']['id']} , type: {type(json['user']['id']).__name__}")

        user = UserRepository.get_user_by_canvas_id(
            jwt_token.canvas_id, db)

        if not user:
            # no user found > create new one and save in db
            # Order matters! TA will get instructor role if it isn't above the instructor in the chain
            if not jwt_token.roles:
                raise OAuth2AuthenticationException(
                    400, "Bad roles", "No roles given in JWT token. Please try reauthenticating via the lti launch")
            roles = []

            for role in jwt_token.roles:
                role = getattr(RolesEnum, role.upper())
                roles.append(RoleRepository.get_role(role, db))

            user = UserModel(fullname=jwt_token.fullname, canvas_email=jwt_token.email,
                             canvas_id=jwt_token.canvas_id, roles=roles, disabled=False)

            db.add(user)
            db.commit()

        jwt_token.access_token = json['access_token']
        jwt_token.refresh_token = json['refresh_token']

        response = RedirectResponse('/')
        response.set_cookie("jwt", jwt_token.encoded_token, max_age=2147483647,
                            httponly=False, samesite="None", secure=True)
        return response
    else:
        raise OAuth2AuthenticationException()


@router.get("/refresh")
async def refresh_token(response: Response, jwt: HTTPAuthorizationCredentials = Depends(token_auth_scheme)):
    """
    Refresh call for getting a new access token from canvas

    Returns a jwt token that should be places in the Authorization header as a Bearer token
    """
    if jwt is None:
        return HTTPException(status_code=400, detail="No jwt token was provided")

    jwt_token = AccessToken.decode_token(jwt.credentials)

    if jwt_token.refresh_token is None:
        return HTTPException(400, "No refresh token was provided")

    r = requests.post(f'{BASE_URL}/login/oauth2/token', data={
        'grant_type': 'refresh_token',
        'client_id': DELEVOPER_KEY_ID,
        'client_secret': DEVELOPER_KEY,
        'refresh_token': jwt_token.refresh_token
    })

    json = r.json()

    """ json ^
    {
        "access_token": str,
        "token_type": "Bearer",
        "user": {
            "id": int, 
            "name": str
        },
        "expires_in": int
    }
    """

    # got the access_token, now check for errors:
    if r.status_code >= 400:
        if r.status_code == 500:
            # Canceled oauth or server error
            raise HTTPException(
                500, "An error occured on the canvas authentication servers. Please refresh the page and try again. Contact support if the issue persists.")
        else:
            raise HTTPException(r.status_code, json)

    jwt_token.access_token = json['access_token']

    response.set_cookie("jwt", jwt_token.encoded_token, max_age=2147483647,
                        httponly=False, samesite="None", secure=True)
    response.body = jwt_token.encoded_token

    return jwt_token.encoded_token
