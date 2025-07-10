from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.responses import RedirectResponse
from app.routes import providers 
from app.database.database import engine, Base

app = FastAPI(
    title="Python Quickstart using FastAPI",
    version="1.0.1",
    description="""
    A quickstart API using Python with  FastAPI 
    """,
    #lifespan=lifespan,
)

# Crear tablas al inicio
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    print("database startups")


app.include_router(providers.router, prefix="/providers", tags=["providers"])


# Redirect to Swagger documentation on loading the API for demo purposes
@app.get("/", include_in_schema=False)
def redirect_to_swagger():
    return RedirectResponse(url="/docs")