from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "sqlite:///project.db"

engine = create_engine(DATABASE_URL, echo=True)
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

def create_db():
    import models.models                 # Імпортуємо моделі, щоб вони були доступні для створення таблиць
    Base.metadata.create_all(bind=engine)

def init_db():
    import models.models                 # Імпортуємо моделі, щоб вони були доступні для створення таблиць
    Base.metadata.create_all(bind=engine)

def drop_db():
    Base.metadata.drop_all(bind=engine)