from sqlalchemy import Column, Integer, String

from database import Base


class RoleModel(Base):
    """RoleModel
    """
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String(length=255), nullable=False,
                        unique=True, index=True)

    def __init__(self, title: str) -> None:
        """RoleModel constructor

        Args:
            title (str): title of the role
        """
        self.title = title
        super().__init__()
