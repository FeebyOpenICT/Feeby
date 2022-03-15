from fastapi import APIRouter, Form, Depends
from Models.Post import Post
from Auth.validate_user import get_current_user
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
    current_user: get_current_user = Depends(get_current_user),
    db: Session = Depends(get_db_connection)

):
    data = Post(body, current_user)
    data.save_self(db)
    return data
