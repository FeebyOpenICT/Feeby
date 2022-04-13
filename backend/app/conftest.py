from fastapi import FastAPI
from fastapi.testclient import TestClient

# necessary for discovery
import pytest


######
# import all routers and exception handlers
from Auth import Authentication
from LTI import lti
from Repositories import RoleRepository, UserRepository
from Controllers import *
from Exceptions import *
######

# Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import drop_database, database_exists

from Auth.validate_user import get_current_active_user
from Schemas import RolesEnum

from database import Base, get_db_connection

######
# import all models that need to be initiated
from Models import *
######


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

    user = UserModel(
        "Alex Duncan",
        "alex.duncan@hu.nl",
        1,
        False,
        [
            RoleRepository.get_role(RolesEnum.ADMIN, db),
            # RolesEnum.CONTENT_DEVELOPER,
            # RolesEnum.INSTRUCTOR,
            # RolesEnum.MENTOR,
            # RolesEnum.OBSERVER,
            # RolesEnum.STUDENT,
            # RolesEnum.TEACHING_ASSISTANT
        ]
    )

    db.add(user)
    db.commit()

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
        user = UserRepository.get_user_by_canvas_id(1, db)
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

    app.include_router(UserRouter)

    app.include_router(PostRouter)

    app.include_router(AspectRouter)

    app.include_router(RatingsRouter)

    app.dependency_overrides[get_db_connection] = override_get_db

    app.dependency_overrides[get_current_active_user] = override_get_current_active_user

    yield TestClient(app)


@pytest.fixture()
def current_active_user(db) -> UserModel:
    user = UserRepository.get_user_by_canvas_id(1, db)
    yield user
