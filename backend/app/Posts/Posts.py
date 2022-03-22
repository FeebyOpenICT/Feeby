from fastapi import APIRouter, Depends, Security
from typing import List
from Models.Post import Post
from Auth.validate_user import get_current_active_user
from sqlalchemy.orm import Session
from Schemas.Post import CreatePost, Post
from database import get_db_connection
from Models.Role import Roles
from Models.User import User
from Schemas.Post import PostInDB

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get('/self',  response_model=List[PostInDB])
async def get_posts(
        current_active_user: User = Security(
            get_current_active_user,
            scopes=[
                Roles.STUDENT['title'],
                Roles.ADMIN['title'],
                Roles.INSTRUCTOR['title'],
                Roles.CONTENT_DEVELOPER['title'],
                Roles.TEACHING_ASSISTANT['title'],
            ]
        ),
        db: Session = Depends(get_db_connection)
):
    """
    Read post from self

    Allowed roles: admin, instructor, student, content_developer, teaching_assistant
    """
    all_posts = Post.get_posts_by_user_id(current_active_user.id, db)
    return all_posts


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
            ]
        ),
        db: Session = Depends(get_db_connection)
):
    """
    Create post

    Allowed roles: admin, instructor, student, content_developer, teaching_assistant
    """
    post = Post(
        title=body.title,
        description=body.description,
        user=current_active_user
    )
    post.save_self(db)
    return post
