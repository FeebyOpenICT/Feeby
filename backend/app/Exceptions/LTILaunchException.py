from fastapi import Request
from fastapi.responses import HTMLResponse


class LTILaunchException(Exception):
    """
    LTI launch exception

    message = message to show the user under the "Login Error" title. Defaults to "An unknown error happened, please refresh the page and try again. Contact support if the issue persists."
    title = Title next to "LTI Launch Error" title. Defaults to None
    """
    status_code = 400

    def __init__(
        self,
        message: str = "An unknown error happened, please refresh the page and try again. Contact support if the issue persists.",
    ):
        self.message = message


async def lti_launch_authentication_exception_handler(request: Request, exc: LTILaunchException):
    """
    Return an authentication error template to the user
    """
    return HTMLResponse(
        status_code=exc.status_code,
        content=f"""
      <body>
        <h1>LTI Launch Error</h1>
        <p>{exc.message}</p>
        <p>This request has been deemed invalid. The request will not proceed for your safety. Please contact support if the issue persists.</p>
      </body>
    """
    )
