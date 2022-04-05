from fastapi import Request, status
from fastapi.responses import JSONResponse


class NotFound(Exception):
    """
    Not found in db exception

    resource = resource name to tell the frontend what type of resource was not found will be formatted as such f"Requested {resource} by identifier: {id} not found in database". example: "user"
    id = identifier
    status_code = HTML status code defaults to 404
    """

    def __init__(self, resource: str, id: int, status_code: int = status.HTTP_404_NOT_FOUND):
        self.resource = resource
        self.id = id
        self.status_code = status_code


async def not_found_exception_handler(request: Request, exc: NotFound):
    """
    Return a json response with error details
    """
    return JSONResponse(
        content={
            "detail": f"Requested {exc.resource}: {exc.id} not found in database",
            "resource": exc.resource,
            "id": exc.id
        },
        status_code=exc.status_code
    )
