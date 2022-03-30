import uvicorn
from fastapi import FastAPI

# import all routers and exception handlers
from Exceptions.AuthenticationException import OAuth2AuthenticationException, oauth2_authentication_exception_handler
from Exceptions.LTILaunchException import LTILaunchException, lti_launch_authentication_exception_handler
from Exceptions.NotFound import NotFound, not_found_exception_handler
from Auth import Authentication
from LTI import lti
from Controllers import UserController
from Posts import Posts
from Aspects import Aspects
from Ratings import Ratings


# import all models that need to be initiated
from Models.Aspect import AspectModel
from Models.Rating import RatingModel
from Models.Aspect_Rating import Aspect_Rating_Model
from Models.User import UserModel
from Models.Role import RoleModel
from Models.User_Role import User_Role_Model
from Models.Post import PostModel


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

app.include_router(lti.router)

app.include_router(Authentication.router)

app.include_router(UserController.router)

app.include_router(Posts.router)

app.include_router(Aspects.router)

app.include_router(Ratings.router)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0",
                port=8000, reload=True, workers=1)
