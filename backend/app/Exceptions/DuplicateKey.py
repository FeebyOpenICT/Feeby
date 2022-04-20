from fastapi import Request, status
from fastapi.responses import JSONResponse


class DuplicateKey(Exception):
    """Duplicate key in database exception
    """

    def __init__(self, resource: str, id: int, status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY):
        """DuplicateKey constructor

        Args:
            resource (str): resource string identifier; per example: "user" | "post" | "aspect"
            id (int): id of resource in database
            status_code (int, optional): HTTP status code. Defaults to status.HTTP_422_UNPROCESSABLE_ENTITY.
        """
        self.resource = resource
        self.id = id
        self.status_code = status_code


async def duplicate_key_exception_handler(request: Request, exc: DuplicateKey):
    """DuplicateKey exception handler for fastapi

    Args:
        request (Request): Fastapi request
        exc (DuplicateKey): raised exception

    Returns:
        JSONResponse: JSON response detailing the occured exception
    """
    return JSONResponse(
        content={
            "detail": f"Cannot create {exc.resource} by identifier: {exc.id} identifier already found in database",
            "resource": exc.resource,
            "id": exc.id
        },
        status_code=exc.status_code
    )
