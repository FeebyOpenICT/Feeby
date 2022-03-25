from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

# necessary for discovery
import pytest


######
from Exceptions.AuthenticationException import OAuth2AuthenticationException, oauth2_authentication_exception_handler
from Exceptions.LTILaunchException import LTILaunchException, lti_launch_authentication_exception_handler
from Auth import Authentication
from LTI import lti
from Models.Role import Role, Roles
from Models.User import User
from Users import users
from Exceptions.NotFound import NotFound, not_found_exception_handler
from Posts import Posts
from Aspects import Aspects
from Ratings import Ratings
######

# Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import drop_database, database_exists

from database import get_db_connection
from Auth.validate_user import get_current_active_user

# Chain: Role > User_Role > User > Post > Rating > Aspect > Aspect_Rating
# Import base from latest in chain so base gets initialized in all models before getting called
# same as in main.py
from Models.Aspect_Rating import Base

# Create the new database session
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture()
def db() -> Session:
    """
    Create db session
    """
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
        "check_same_thread": False})

    assert not database_exists(SQLALCHEMY_DATABASE_URL)

    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine)

    db = TestingSessionLocal()

    user = User(
        "Alex Duncan",
        "alex.duncan@hu.nl",
        1,
        False,
        [
            Role.get_role(Roles.ADMIN, db),
            # Roles.CONTENT_DEVELOPER,
            # Roles.INSTRUCTOR,
            # Roles.MENTOR,
            # Roles.OBSERVER,
            # Roles.STUDENT,
            # Roles.TEACHING_ASSISTANT
        ]
    )

    user.save_self(db)

    try:
        yield db
    finally:
        db.close()
        drop_database(SQLALCHEMY_DATABASE_URL)


@pytest.fixture()
def client(db):
    """
    Dependency overrides
    """

    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    def override_get_current_active_user():
        user = User.get_user_by_canvas_id(1, db)
        return user

    # Cant import from main.py, will result in Postgres being used for some reason. Placing it in a seperate file and function also does not work
    app = FastAPI()

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

    app.dependency_overrides[get_db_connection] = override_get_db

    app.dependency_overrides[get_current_active_user] = override_get_current_active_user

    yield TestClient(app)


@pytest.fixture()
def current_active_user(db) -> User:
    user = User.get_user_by_canvas_id(1, db)
    yield user
