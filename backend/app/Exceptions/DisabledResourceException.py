from fastapi import Request, status
from fastapi.responses import JSONResponse


class DisabledResourceException(Exception):
    """DisabledResourceException
    """

    def __init__(self, resource: str, id: int, status_code: int = status.HTTP_410_GONE):
        """DisabledResourceException constructor

         Args:
             resource (str): resource string identifier; per example: "user" | "post" | "aspect"
             id (int): id of resource in database
             status_code (int, optional): HTTP status code. Defaults to status.HTTP_404_NOT_FOUND.
         """
        self.resource = resource
        self.id = id
        self.status_code = status_code


async def disabled_resource_exception_handler(request: Request, exc: DisabledResourceException):
    """DisabledResourceException exception handler for fastapi

     Args:
         request (Request): Fastapi request
         exc (NotFound): raised exception

     Returns:
         JSONResponse: JSON response detailing the occured exception
     """
    return JSONResponse(
        content={
            "detail": f"Requested {exc.resource}: {exc.id} has been disabled",
            "resource": exc.resource,
            "id": exc.id
        },
        status_code=exc.status_code
    )
