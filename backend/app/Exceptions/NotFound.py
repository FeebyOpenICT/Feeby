from fastapi import status
from fastapi.responses import ORJSONResponse

class NotFound(Exception):
  """
  Not found in db exception

  item = item name to tell the frontend what type of item was not found will be formatted as such f"Requested {item} not found in database". example: "user"
  status_code = HTML status code defaults to 404
  """
  def __init__(self, item: str = "Requested resource not found in database", status_code: int = status.HTTP_404_NOT_FOUND):
    self.item = item
    self.status_code = status_code


async def not_found_exception_handler(exc: NotFound):
  """
  Return a json response with error and 
  """
  return ORJSONResponse(
    content={
      "detail": f"Requested {exc.item} not found in database",
    },
    status_code=exc.status_code
  )
