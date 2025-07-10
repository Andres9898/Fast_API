# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Obtener URL desde .env
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)
# Crear el engine de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)  # echo=True para ver las consultas en consola

# Crear session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()

# Dependency para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
