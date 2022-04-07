from fastapi import Request, status
from fastapi.responses import JSONResponse


class DuplicateKey(Exception):
    """
    Duplicate key in db

    resource = resource name that tried to insert a duplicate key, will be formatted as such f"Cannot create {resource} by identifier: {id} identifier already found in database". example: "user"
    id = identifier
    status_code = HTML status code defaults to 422
    """

    def __init__(self, resource: str, id: int, status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY):
        self.resource = resource
        self.id = id
        self.status_code = status_code


async def duplicate_key_exception_handler(request: Request, exc: DuplicateKey):
    """
    Return a json response with error details
    """
    return JSONResponse(
        content={
            "detail": f"Cannot create {exc.resource} by identifier: {exc.id} identifier already found in database",
            "resource": exc.resource,
            "id": exc.id
        },
        status_code=exc.status_code
    )
