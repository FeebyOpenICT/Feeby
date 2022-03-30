from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
    SecurityScopes,
)

from Repositories.User import UserRepository

from .JWTToken import AccessToken
from Models.User import UserModel
from database import get_db_connection

# automatically checks if there is a Bearer token in the Authorization header
# Cant use OAuth2AuthorizationCodeBearer from fastapi.security because it requires a url to create a token and log in at. \
# we get the token from canvas so we can't do that.
token_auth_scheme = HTTPBearer()


async def get_current_user(
    security_scopes: SecurityScopes,
    jwt_token: HTTPAuthorizationCredentials = Depends(token_auth_scheme),
    db: Session = Depends(get_db_connection),
) -> UserModel:
    """
    Gets the current user from the database by decoding the jwt bearer token

    Also checks allowed roles

    Returns the User mapped class
    """
    token = AccessToken.decode_token(jwt_token.credentials)

    if security_scopes.scopes:
        scopes = security_scopes.scopes

        if scopes and not token.roles:
            # no roles in token, something went wrong whilst making the token.
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="No roles found in jwt token")

        has_required_role = False

        for token_role in token.roles:
            if token_role in scopes:
                # user has one of the required roles so no need to check any further roles
                has_required_role = True
                break

        if has_required_role == False:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Not enough permissions")

    # validate access token against canvas
    canvas_user = token.validate_self()

    user = UserRepository.get_user_by_canvas_id(canvas_user['id'], db)

    return user


async def get_current_active_user(
    current_user: UserModel = Security(get_current_user, scopes=[])
) -> UserModel:
    """
    Gets current active user thats making an api request

    returns the User mapped class 
    raises unauthenticated exception if the user is disabled in the database
    """
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive User")
    return current_user
