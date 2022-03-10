from typing import Optional
from fastapi import APIRouter, Cookie, Form, Depends
from fastapi.responses import RedirectResponse
from datetime import datetime, timedelta

from Auth.redir_to_auth import redir_to_oauth
from Exceptions.LTILaunchException import LTILaunchException
from config import CLIENT_ID

router = APIRouter(
  prefix="/lti",
  tags=["L.T.I."]
)

oauth_nonce_timestamps = {}

@router.post('/launch')
async def launch(
  user_id: str = Form(...),
  ext_roles: str = Form(...),
  jwt: Optional[str] = Cookie(None),
  roles: str = Form(...),
  oauth_callback: str = Form(...),
  oauth_consumer_key: str = Form(...),
  oauth_nonce: str = Form(...),
  oauth_signature: str = Form(...),
  oauth_signature_method: str = Form(...),
  oauth_timestamp: str = Form(...),
  oauth_version: str = Form(...),
  # db: Session = Depends(get_db_connection)
):
  """
  Launch call for canvas

  Verify if LTI launch is valid
  
  redir to auth if no jwt token cookie can be found.

  No jwt cookie means that the user has never authorized before and has to do it first.
  """
  if oauth_callback != "about:blank":
    raise LTILaunchException("oauth_callback does not match 'about:blank'")
  
  if oauth_consumer_key != CLIENT_ID:
    raise LTILaunchException("oauth_consumer_key does not match the CLIENT_ID")

  if oauth_version != "1.0":
    raise LTILaunchException("Oauth version does not match '1.0'")

  try:
    date_oauth_timestamp = datetime.fromtimestamp(int(oauth_timestamp))
    now = datetime.now()
    five_minutes = timedelta(minutes=5)
    if date_oauth_timestamp < (now - five_minutes):
      raise LTILaunchException("oauth_timestamp is older than 5 minutes")
  except:
    raise LTILaunchException("Could not compare oauth_timestamp time")

  # TODO Setup redis and check if oauth_nonce has been used in the last five minutes based upon the oauth_timestamp
  # key = timestamp; value = oauth_nonce

  # TODO check oauth url 

  # TODO check against user_id from launch req. in jwt
  # possibly use user_id in db instead of canvas_id from /api/v1/users/self ?
  
  if jwt is not None:
    # user has already got the access and refresh tokens once before so no need to reauth
    return RedirectResponse('/')

  return redir_to_oauth()
