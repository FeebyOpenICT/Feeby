from fastapi import status
from fastapi.responses import RedirectResponse

from config import BASE_CANVAS_URL, BASE_APP_API_CALLBACK_URL, DELEVOPER_KEY_ID


def redir_to_oauth() -> RedirectResponse:
    """
    Redirects the user to Oauth2 flow from canvas

    Returns a RedirectResponse from fastapi.responses formatted to the /login/oauth2 call for canvas
    """
    print("Redirecting to auth")
    return RedirectResponse(
        f'{BASE_CANVAS_URL}/login/oauth2/auth?client_id={DELEVOPER_KEY_ID}&response_type=code&state=aaaaaa&redirect_uri={BASE_APP_API_CALLBACK_URL}',
        status_code=status.HTTP_302_FOUND
    )
