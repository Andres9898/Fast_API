from fastapi import APIRouter, Form, HTTPException, Depends
import config
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.providers import Provider
from app.schemas.providers import ProviderCreate, ProviderOut
from typing import List

router = APIRouter(prefix="/providers", tags=["providers"])

@router.get("/", response_model=List[ProviderOut])
def get_providers(db: Session = Depends(get_db)):
    try:
        results = db.query(Provider).all()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener proveedores: {str(e)}")

@router.post("/", response_model=ProviderOut)
def create_provider(provider: ProviderCreate, db: Session = Depends(get_db)):
    db_provider = Provider(**provider.dict())
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
    return db_provider