from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import RedirectResponse
import requests

from . import redir_to_auth
from config import BASE_APP_API_URL, BASE_URL

class CheckValidUser(BaseHTTPMiddleware):
  async def dispatch(self, request: Request, call_next):
    if request.cookies['access_token']:
      headers = {
        "Authorization": f"Bearer {request.cookies['access_token']}"
      }
      r = requests.get(f'{BASE_URL}/api/v1/users/self', headers=headers)
      json = r.json()

      print(json)

      response = await call_next(request)

      return response
    elif request.cookies['refresh_token']:
      return RedirectResponse(f'{BASE_APP_API_URL}/auth/refresh')
    elif not request.cookies['access_token']:
      return redir_to_auth()
