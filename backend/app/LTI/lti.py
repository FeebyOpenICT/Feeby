from multiprocessing.sharedctypes import Value
from typing import Optional
from fastapi import APIRouter, Cookie, Form, Depends, Request, Response
from fastapi.responses import RedirectResponse
from datetime import datetime, timedelta
import urllib.parse
from hashlib import sha1
import hmac
import base64

from Auth.redir_to_auth import redir_to_oauth
from Exceptions.LTILaunchException import LTILaunchException
from Auth.JWTToken import AccessToken
from config import CLIENT_SECRET, DEVELOPER_KEY, CLIENT_ID
from redis_client import redis_client

router = APIRouter(
  prefix="/lti",
  tags=["L.T.I."]
)

@router.post('/launch', response_class=RedirectResponse)
async def launch(
  request: Request,
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
  # Verify oauth1 call
  # See these resources for a good step by step guide or general idea for how its done
  # https://developer.twitter.com/en/docs/authentication/oauth-1-0a/creating-a-signature
  # https://community.canvaslms.com/t5/Canvas-Developers-Group/LTI-OAUTH-1-0-Signature-Mismatch/td-p/167363
  # http://www.imsglobal.org/specs/ltiv1p0/implementation-guide#:~:text=4.2%C2%A0%C2%A0%C2%A0%C2%A0%C2%A0%C2%A0-,Basic%20LTI%20Message%20Signing,-Move%20to%20top

  if oauth_callback != "about:blank":
    raise LTILaunchException("oauth_callback does not match 'about:blank'")
  
  if oauth_consumer_key != CLIENT_ID:
    raise LTILaunchException("oauth_consumer_key does not match the CLIENT_ID")

  if oauth_version != "1.0":
    raise LTILaunchException("Oauth version does not match '1.0'")

  if oauth_signature_method != 'HMAC-SHA1':
    raise LTILaunchException("oauth_signature_method does not match 'HMAC-SHA1'")

  try:
    date_oauth_timestamp = datetime.fromtimestamp(int(oauth_timestamp))
    now = datetime.now()
    five_minutes = timedelta(minutes=5)
    if date_oauth_timestamp < (now - five_minutes):
      raise LTILaunchException("oauth_timestamp is older than 5 minutes")
  except:
    raise LTILaunchException("Could not compare oauth_timestamp time")

  cached_oauth_nonce = redis_client.get(oauth_timestamp)
  if cached_oauth_nonce:
    if oauth_nonce == cached_oauth_nonce:
      raise LTILaunchException("oauth_nonce signature has already been made in the last five minutes")

  redis_client.setex(name=oauth_timestamp, time=five_minutes, value=oauth_nonce)


  http_method = "POST"
  base_url = request.url._url
  paramaters = []

  for key, value in request._form.items():
    # encode all but the oauth_signature
    if key != 'oauth_signature':
      paramaters.append(f"{key}={value}")
  
  paramaters.sort()

  paramaters = list(map(lambda param: urllib.parse.quote(param, safe='='), paramaters))
  
  paramaters = '&'.join(paramaters)

  signature_base = f"{http_method}&{urllib.parse.quote(base_url, '')}&{urllib.parse.quote(paramaters, '')}"

  signing_key = f"{urllib.parse.quote(CLIENT_SECRET, '')}&" # See second canvas link

  hashed = hmac.new(key=bytes(signing_key, 'utf-8'), msg=bytes(signature_base, 'utf-8'), digestmod=sha1)
  signature = str(base64.b64encode(hashed.digest()), 'utf-8').rstrip('\n')

  if oauth_signature != signature:
    raise LTILaunchException(f"oauth_signature: {oauth_signature} does not match calculated signature: {signature}")

  # Check jwt token
  redir_to_auth_response = redir_to_oauth()
  if jwt == None:
    jwt_token = AccessToken(access_token=None, refresh_token=None, canvas_id=user_id, roles=ext_roles.split(','))
    redir_to_auth_response.set_cookie("jwt", jwt_token.encoded_token, max_age=2147483647, httponly=False, samesite="None", secure=True)
    return redir_to_auth_response
  else:
    # user has already got the access and refresh tokens once before so no need to reauth
    # check if user making launch request is user that is logging in
    jwt_token = AccessToken.decode_token(jwt)

    redir_to_auth_response.set_cookie("jwt", jwt_token.encoded_token, max_age=2147483647, httponly=False, samesite="None", secure=True)

    if jwt_token.canvas_id != user_id or jwt_token.refresh_token == None:
      return redir_to_auth_response

    return RedirectResponse('/')
