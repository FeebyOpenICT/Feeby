from sqlalchemy.orm import Session


class SaveableModel:
    def save_self(self, db: Session):
        """
        Saves own instance in database

        returns own saved instance mapped class
        """
        db.add(self)
        db.commit()
        db.refresh(self)
        return self
