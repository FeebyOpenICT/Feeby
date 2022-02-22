from fastapi import responses, status

from config import BASE_URL, BASE_APP_API_CALLBACK_URL, DELEVOPER_KEY_ID

def redir_to_oauth():
  """
  Redirects the user to Oauth2 flow from canvas
  """
  print("Redirecting to auth")
  return responses.RedirectResponse(
      f'{BASE_URL}/login/oauth2/auth?client_id={DELEVOPER_KEY_ID}&response_type=code&state=aaaaaa&redirect_uri={BASE_APP_API_CALLBACK_URL}',
      status_code=status.HTTP_302_FOUND
    )
