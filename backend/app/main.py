import uvicorn
from fastapi import Depends, FastAPI

from Exceptions.AuthenticationException import OAuth2AuthenticationException, oauth2_authentication_exception_handler
from Exceptions.LTILaunchException import LTILaunchException, lti_launch_authentication_exception_handler
from Exceptions.NotFound import NotFound, not_found_exception_handler
from Auth import Authentication
from LTI import lti
from Users import users
from Posts import Posts
from Aspects import Aspects
from Ratings import Ratings


from database import engine
# Chain: Role > User_Role > User > Post > Aspect > AspectRating
# Import base from latest in chain so base gets initialized in all models before getting called
# same as in test_main
from Models.Rating import Base

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

app.include_router(lti.router)

app.include_router(Authentication.router)

app.include_router(users.router)

app.include_router(Posts.router)

app.include_router(Aspects.router)

app.include_router(Ratings.router)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0",
                port=8000, reload=True, workers=1)
