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
from Aspect import Aspects
######

# Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from database import get_db_connection
from Auth.validate_user import get_current_active_user
from Models.Post import Base

# Create the new database session
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def db() -> Session:
    """
    Create db session
    """

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

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

    app.dependency_overrides[get_db_connection] = override_get_db

    app.dependency_overrides[get_current_active_user] = override_get_current_active_user

    yield TestClient(app)


@pytest.fixture()
def current_active_user(db) -> User:
    user = User.get_user_by_canvas_id(1, db)
    yield user
