import uvicorn
from fastapi import Depends, FastAPI

from Exceptions.AuthenticationException import OAuth2AuthenticationException, oauth2_authentication_exception_handler
from Exceptions.LTILaunchException import LTILaunchException, lti_launch_authentication_exception_handler
from Auth import Authentication
from LTI import lti
from Auth.validate_user import get_current_active_user


from database import engine

# Chain: Role > User
# Import base from latest in chain so base gets initialized in all models before getting called
from Models.User import Base

# Create all tables in database
Base.metadata.create_all(bind=engine)

# Init fastapi
app = FastAPI(
    title="Feeby",
    version=1,
    root_path="/api/v1" # Docker
)

app.add_exception_handler(OAuth2AuthenticationException, oauth2_authentication_exception_handler)

app.add_exception_handler(LTILaunchException, lti_launch_authentication_exception_handler)

app.include_router(lti.router)

app.include_router(Authentication.router)
 
@app.get("/users/self")
async def read_users_me(current_user = Depends(get_current_active_user)):
    return current_user

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True, workers=1)
