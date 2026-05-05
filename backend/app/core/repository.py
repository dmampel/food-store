from typing import Generic, List, Optional, Type, TypeVar
from sqlmodel import Session, select, func
from datetime import datetime

T = TypeVar("T")

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], session: Session):
        self.model = model
        self.session = session

    def get_by_id(self, entity_id: int) -> Optional[T]:
        return self.session.get(self.model, entity_id)

    def list_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        # Filter out soft-deleted items if the model has deleted_at
        statement = select(self.model)
        if hasattr(self.model, "deleted_at"):
            statement = statement.where(getattr(self.model, "deleted_at") == None)
        
        statement = statement.offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def count(self) -> int:
        statement = select(func.count()).select_from(self.model)
        if hasattr(self.model, "deleted_at"):
            statement = statement.where(getattr(self.model, "deleted_at") == None)
        return self.session.exec(statement).one()

    def create(self, entity: T) -> T:
        self.session.add(entity)
        self.session.flush()
        self.session.refresh(entity)
        return entity

    def update(self, entity: T) -> T:
        self.session.add(entity)
        self.session.flush()
        self.session.refresh(entity)
        return entity

    def soft_delete(self, entity: T) -> None:
        if hasattr(entity, "deleted_at"):
            setattr(entity, "deleted_at", datetime.utcnow())
            self.session.add(entity)
            self.session.flush()
        else:
            raise AttributeError(f"Model {self.model.__name__} does not support soft delete")

    def hard_delete(self, entity: T) -> None:
        self.session.delete(entity)
        self.session.flush()
