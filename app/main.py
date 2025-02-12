from fastapi import FastAPI
from app.api.routes.auth import auth_router

app = FastAPI(title="FastAPI Auth with MongoDB")

app.include_router(auth_router, prefix="/auth")

@app.get("/")
def root():
    return {"message": "FastAPI Authentication with MongoDB"}
