from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, registry

# Импортируем настройки из config
from config.settings import DATABASE_URL
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
_registry = registry()
_registry.configure()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
