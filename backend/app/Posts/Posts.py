from fastapi import APIRouter, Depends
from Models.Post import Post
from Auth.validate_user import get_current_active_user
from sqlalchemy.orm import Session
from Schemas.Post import PostBody
from database import get_db_connection

router = APIRouter(
    prefix="/post",
    tags=["StudentPost"]
)


@router.post('/')
async def post(
    body: PostBody,
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
