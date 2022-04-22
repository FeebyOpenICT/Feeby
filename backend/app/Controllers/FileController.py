from fastapi import APIRouter, status, Depends, Security
from Schemas import FileInDB
from database import get_db_connection
from Auth.validate_user import get_current_active_user
from sqlalchemy.orm import Session
from Models import UserModel

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.post('', response_model=FileInDB, status_code=status.HTTP_201_CREATED)
async def create_upload_file(
        current_active_user: UserModel = Depends(get_current_active_user),
        db: Session = Depends(get_db_connection)
):
    """Upload a file

    Allowed roles:
    - All
    """


