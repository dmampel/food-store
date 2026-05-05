from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=False,  # Set to True to log SQL queries
    pool_pre_ping=True
)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    # This will be replaced by Alembic in production
    # But useful for initial prototyping
    SQLModel.metadata.create_all(engine)
