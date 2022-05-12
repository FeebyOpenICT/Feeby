from fastapi import Request, status
from fastapi.responses import JSONResponse


class DoesNotBelongTo(Exception):
    """Does not belong to in database exception
    """

    def __init__(self, parentResource: str, parentId: int, resource: str, id: int, status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY):
        """DoesNotBelongTo constructor

        Args:
            resource (str): resource string identifier; per example: "user" | "post" | "aspect"
            id (int): id of resource in database
            status_code (int, optional): HTTP status code. Defaults to status.HTTP_422_UNPROCESSABLE_ENTITY.
        """
        self.parentResource = parentResource
        self.resource = resource
        self.id = id
        self.status_code = status_code
        self.parentId = parentId


async def does_not_belong_to_exception_handler(request: Request, exc: DoesNotBelongTo):
    """DoesNotBelongTo exception handler for fastapi

    Args:
        request (Request): Fastapi request
        exc (DoesNotBelongTo): raised exception

    Returns:
        JSONResponse: JSON response detailing the occured exception
    """
    return JSONResponse(
        content={
            "detail": f"Resource {exc.resource} by identifier: {exc.id} does not belong to {exc.parentResource} by identifier: {exc.parentId}",
            "resource": exc.resource,
            "id": exc.id,
            "parentResource": exc.parentResource,
            "parentId": exc.parentId
        },
        status_code=exc.status_code
    )
