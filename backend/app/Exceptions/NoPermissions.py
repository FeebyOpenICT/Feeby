from fastapi import Request, status
from fastapi.responses import JSONResponse


class NoPermissions(Exception):
    """No permissions error
    """

    def __init__(self, resource: str, id: int, status_code: int = status.HTTP_403_FORBIDDEN):
        """NoPermissions constructor

        Args:
            resource (str): resource string identifier; per example: "user" | "post" | "aspect"
            id (int): id of resource in database
            status_code (int, optional): HTTP status code. Defaults to status.HTTP_403_FORBIDDEN
        """
        self.resource = resource
        self.id = id
        self.status_code = status_code


async def no_permissions_exception_handler(request: Request, exc: NoPermissions):
    """NoPermissions exception handler for fastapi

    Args:
        request (Request): Fastapi request
        exc (NoPermissions): raised exception

    Returns:
        JSONResponse: JSON response detailing the occured exception
    """
    return JSONResponse(
        content={
            "detail": f"You do not have the required permissions to access the requested {exc.resource}: {exc.id} resource",
            "resource": exc.resource,
            "id": exc.id
        },
        status_code=exc.status_code
    )
