from sqlmodel import Session
from app.db.database import engine
from typing import Type, TypeVar

class UnitOfWork:
    def __init__(self):
        self.session_factory = lambda: Session(engine)

    def __enter__(self):
        self.session = self.session_factory()
        # Initialize repositories here as they are created
        # self.users = UserRepository(self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.session.commit()
            else:
                self.session.rollback()
        finally:
            self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
