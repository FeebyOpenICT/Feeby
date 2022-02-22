from fastapi import APIRouter, Form
import requests

from .redir_to_auth import redir_to_oauth
from ..Exceptions.AuthenticationException import OAuth2AuthenticationException
from ..config import BASE_URL, DELEVOPER_KEY_ID, DEVELOPER_KEY, BASE_APP_API_URL


router = APIRouter(
  prefix="/auth",
  tags="Authentication",
)

# temp fake db
users = {}

@router.post("/launch")
async def launch(user_id: str = Form(...)):
    # Ceck if user already exists in db
    if user_id in users:
        # if True get refresh token from db and get token that way to avoid having to re log in
        return redir_to_oauth() #temp redir for dev testing
    else:
        # if False send user to auth flow 
        # create user in db and set auth
        return redir_to_oauth()


@router.get("/callback")
async def launch(code: str = None, error: str = None, error_description: str = None):
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
            'redirect_uri': f'{BASE_APP_API_URL}/callback',
            'code': code
        })
        # got the access_token, now check for errors:
        if r.status_code == 500:
            # Canceled oauth or server error
            raise OAuth2AuthenticationException(status_code=500, message="An error occured on the canvas authentication servers. Please refresh the page and try again. Contact support if the issue persists.")
        json = r.json()
        return json
    else:
        raise OAuth2AuthenticationException()
