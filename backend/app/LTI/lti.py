from fastapi import APIRouter, Form

from Auth.redir_to_auth import redir_to_oauth

router = APIRouter(
  prefix="/lti",
  tags=["L.T.I."]
)

@router.post('/launch')
async def launch(user_id: str = Form(...)):
  # check if user is in db and skip auth if they are. 
  # if user_id in users:
  #     # if True get refresh token from db and get token that way to avoid having to re log in
  #     return redir_to_oauth() #temp redir for dev testing
  # else:
  #     # if False send user to auth flow 
  #     # create user in db and set auth
  #     return redir_to_oauth()
  return redir_to_oauth()
