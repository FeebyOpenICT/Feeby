from fastapi import APIRouter, Form, Depends
from sqlalchemy.orm import Session
import requests

from Exceptions.AuthenticationException import OAuth2AuthenticationException

from database import get_db_connection
from config import BASE_URL, DELEVOPER_KEY_ID, DEVELOPER_KEY, BASE_APP_API_CALLBACK_URL
from Models.User import User, Student

router = APIRouter(
  prefix="/auth",
  tags=["Authentication"],
)

@router.get("/callback")
async def callback(code: str = None, error: str = None, error_description: str = None, db: Session = Depends(get_db_connection)):
    """
    Callback for oauth2 flow https://canvas.instructure.com/doc/api/file.oauth.html
    """
    if error:
        # Something went wrong or the user denied access
        if error_description:
            raise OAuth2AuthenticationException(message=error_description)
        raise OAuth2AuthenticationException(title=error)
    elif code:
        # Got the code, still need to check if the state has been tempered with.
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
                raise OAuth2AuthenticationException(status_code=500, message="An error occured on the canvas authentication servers. Please refresh the page and try again. Contact support if the issue persists.")
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
        user = db.query(User).filter(User.canvas_id == json["user"]["id"]).first()

        if user:
            # user found
            return user
        else:
            # no user found > create new one
            self = requests.get(f'{BASE_URL}/api/v1/users/self', headers={ 'Authorization': f'Bearer {json["access_token"]}' })
            self_json = self.json()
            new_user = Student(db=db, fullname=self_json["name"], canvas_id=json["user"]["id"])
            return new_user.save_self(db)

    else:
        raise OAuth2AuthenticationException()


#TODO refresh token call

#TODO decorator/ global middleware to check access token on each api call