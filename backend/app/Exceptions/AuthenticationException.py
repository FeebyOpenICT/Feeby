from fastapi import Request, status
from fastapi.responses import HTMLResponse


class OAuth2AuthenticationException(Exception):
    """OAuth2 exception during LTI launch, returns html template to user
    """

    def __init__(self, status_code=status.HTTP_401_UNAUTHORIZED, title: str = None, message: str = "An unknown error happened, please refresh the page and try again. Contact support if the issue persists."):
        """OAuth2AuthenticationException constructor

        Args:
            status_code (int, optional): HTTP status code. Defaults to status.HTTP_401_UNAUTHORIZED.
            title (str, optional): Custom HTML Title at the top of the screen next to "Login Error:". Defaults to None.
            message (str, optional): Custom error message. Defaults to "An unknown error happened, please refresh the page and try again. Contact support if the issue persists.".
        """
        self.message = message
        self.status_code = status_code
        self.title = title


async def oauth2_authentication_exception_handler(request: Request, exc: OAuth2AuthenticationException):
    """OAuth2 exception handler for fastapi

    Args:
        request (Request): Fastapi request
        exc (OAuth2AuthenticationException): raised exception

    Returns:
        HTML template: returns an html template for the client to render
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
