from fastapi import APIRouter, Form, HTTPException, Depends
import config
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.providers import Provider
from app.schemas.providers import ProviderCreate, ProviderOut

router = APIRouter(prefix="/providers", tags=["providers"])

@router.get("/")
def get_providers():
    try:
        #take from db all providers
        results = ("nothing done")
        
        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar imágenes: {str(e)}")

@router.post("/", response_model=ProviderOut)
def create_provider(provider: ProviderCreate, db: Session = Depends(get_db)):
    db_provider = Provider(**provider.dict())
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
    return db_provider