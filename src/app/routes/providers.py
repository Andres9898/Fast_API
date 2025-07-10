from fastapi import APIRouter, Form, HTTPException
import config

router = APIRouter()

@router.get("/")
def get_providers():
    try:
        #take from db all providers
        results = ("nothing done")
        
        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar imágenes: {str(e)}")
