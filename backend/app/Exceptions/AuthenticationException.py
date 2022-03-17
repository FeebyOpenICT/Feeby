from fastapi import Request
from fastapi.responses import HTMLResponse


class OAuth2AuthenticationException(Exception):
    """
    Authentication exception

    status_code = an html error status code, should probably be 401 or 403 for this error
    message = message to show the user under the "Login Error" title. Defaults to "An unknown error happened, please refresh the page and try again. Contact support if the issue persists."
    title = Title next to "Login Error" title. Defaults to None
    """

    def __init__(self, status_code=401, title: str = None, message: str = "An unknown error happened, please refresh the page and try again. Contact support if the issue persists."):
        self.message = message
        self.status_code = status_code
        self.title = title


async def oauth2_authentication_exception_handler(request: Request, exc: OAuth2AuthenticationException):
    """
    Return an authentication error template to the user
    """
    return HTMLResponse(
        status_code=exc.status_code,
        content=f"""
      <body>
        <h1>Login Error: {exc.title}</h1>
        <div>{exc.message}</div>
      </body>
    """
    )
