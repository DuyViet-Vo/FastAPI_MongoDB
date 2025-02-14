from fastapi import FastAPI

from app.api.routes.auth import auth_router


def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI Build By Võ Duy Việt")
    app.include_router(auth_router, prefix="/auth")

    @app.get("/")
    def root():
        return {"message": "FastAPI Authentication with MongoDB"}

    return app
