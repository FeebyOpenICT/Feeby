import uvicorn
from fastapi import FastAPI

# import all routers and exception handlers
from Exceptions import *
from Auth import Authentication
from LTI import lti
from Controllers import UserRouter, PostRouter, AspectRouter
from Ratings import Ratings


# import all models that need to be initiated
from Models import *


# import database
from database import engine, Base

# Create all tables in database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Feeby",
    version=1,
    root_path="/api/v1"  # Docker
)

app.add_exception_handler(OAuth2AuthenticationException,
                          oauth2_authentication_exception_handler)

app.add_exception_handler(
    LTILaunchException, lti_launch_authentication_exception_handler)

app.add_exception_handler(NotFound, not_found_exception_handler)

app.add_exception_handler(DuplicateKey, duplicate_key_exception_handler)

app.include_router(lti.router)

app.include_router(Authentication.router)

app.include_router(UserRouter)

app.include_router(PostRouter)

app.include_router(AspectRouter)

app.include_router(Ratings.router)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0",
                port=8000, reload=True, workers=1)
