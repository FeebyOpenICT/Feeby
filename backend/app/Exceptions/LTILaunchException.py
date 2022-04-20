from fastapi import Request, status
from fastapi.responses import HTMLResponse


class LTILaunchException(Exception):
    """LTI Launch exception during LTI launch, returns html template to user
    """

    def __init__(
        self,
        message: str = "An unknown error happened, please refresh the page and try again. Contact support if the issue persists.",
        status_code: int = status.HTTP_400_BAD_REQUEST
    ):
        """LTILaunchException constructor

        Args:
            message (str, optional): Custom error message. Defaults to "An unknown error happened, please refresh the page and try again. Contact support if the issue persists.".
            status_code (int, optional): HTTP status code. Defaults to status.HTTP_400_BAD_REQUEST.
        """
        self.status_code = status_code
        self.message = message


async def lti_launch_authentication_exception_handler(request: Request, exc: LTILaunchException):
    """LTI Launch exception handler for fastapi

    Args:
        request (Request): Fastapi request
        exc (LTILaunchException): raised exception

    Returns:
        HTML template: returns an html template for the client to render
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
