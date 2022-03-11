from fastapi import APIRouter, Form, Depends, Response
from starlette import status
from sqlalchemy.orm import Session
from database import get_db_connection
from Models.Post import Post
from Auth.validate_user import get_current_user

router = APIRouter(
    prefix="/post",
    tags=["P.O.S.T."]
)


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED
    # response_model=Post
)
async def post(
        title: str = Form(...),
        description: str = Form(...),
        user_id: get_current_user = Depends(get_current_user),
        db: Session = Depends(get_db_connection)
):
    return post()
