import uvicorn
from fastapi import FastAPI

from Auth import Authentication
from Controllers import *
# import all routers and exception handlers
from Exceptions import *
from LTI import lti
# import database
from database import engine, Base

# import all models that need to be initiated

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

app.add_exception_handler(NotFoundException, not_found_exception_handler)

app.add_exception_handler(DuplicateKey, duplicate_key_exception_handler)

app.add_exception_handler(DisabledResourceException,
                          disabled_resource_exception_handler)

app.add_exception_handler(NoPermissions, no_permissions_exception_handler)

app.add_exception_handler(
    DoesNotBelongTo, does_not_belong_to_exception_handler)

app.include_router(lti.router)

app.include_router(Authentication.router)

app.include_router(UserRouter)

app.include_router(PostRouter)

app.include_router(AspectRouter)

app.include_router(RatingsRouter)

app.include_router(RevisionRouter)

app.include_router(FeedbackRouter)

app.include_router(InviteRouter)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0",
                port=8000, reload=True, workers=1)
