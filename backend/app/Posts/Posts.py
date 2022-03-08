from fastapi import APIRouter, Form, Depends
from sqlalchemy.orm import Session
from database import get_db_connection
from Models.Post import Post
from Models.User import Student


router = APIRouter(
  prefix="/post",
  tags=["P.O.S.T."]
)

@router.post('/')
async def post(
   title: str = Form(...),
   description: str = Form(...),
   db: Session = Depends(get_db_connection)
):
   user = Student()
  return