from fastapi import APIRouter, Depends, Security
from Models.Post import Post
from Auth.validate_user import get_current_active_user
from sqlalchemy.orm import Session
from Schemas.Post import CreatePost
from database import get_db_connection
from Models.Role import Roles
from Models.User import User
from Schemas.Post import PostInDB


router = APIRouter(
    prefix="/post",
    tags=["StudentPost"]
)


@router.post('/', response_model=PostInDB)
async def post(
    body: CreatePost,
    current_active_user: User = Security(
        get_current_active_user,
        scopes=[
          Roles.STUDENT['title'],
          Roles.ADMIN['title'],
          Roles.INSTRUCTOR['title'],
          Roles.CONTENT_DEVELOPER['title'],
          Roles.TEACHING_ASSISTANT['title'],
          Roles.OBSERVER['title'],
        ]
    ),
    user: get_current_active_user = Depends(get_current_active_user),
    db: Session = Depends(get_db_connection)
):
    post = Post(
        title=body.title,
        description=body.description,
        user=user
    )
    post.save_self(db)
    return post
