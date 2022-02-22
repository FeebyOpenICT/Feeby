import uvicorn
from fastapi import FastAPI, Form, Request

from Exceptions.AuthenticationException import OAuth2AuthenticationException, oauth2_authentication_exception_handler
from Auth import Authentication
from LTI import lti

app = FastAPI(
    title="Feeby",
    version=1,
    # root_path="/api/v1" # Docker
)

app.add_exception_handler(OAuth2AuthenticationException, oauth2_authentication_exception_handler)

app.include_router(lti.router)
app.include_router(Authentication.router)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True, workers=1)
