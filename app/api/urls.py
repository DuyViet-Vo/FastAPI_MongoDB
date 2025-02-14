from fastapi import FastAPI

from app.api.routes.auth import auth_router
from app.api.routes.product_routes import router as product_router


def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI Build By Võ Duy Việt")
    app.include_router(auth_router, prefix="/auth")
    app.include_router(product_router, prefix="/api")

    @app.get("/")
    def root():
        return {"message": "FastAPI Authentication with MongoDB"}

    return app
