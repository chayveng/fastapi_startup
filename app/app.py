from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.routes import routers as v1_routers
from app.core.config import configs
from app.util.class_object import singleton


@singleton
class AppCreator:
    def __init__(self) -> None:
        self.app = FastAPI(
            title="FastAPI Startup",
            openapi_url="/api/openapi.json",
            version="0.0.1"
        )

        if configs.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        @self.app.get("/")
        def root():
            return {"message": "Hello, FastAPI"}

        self.app.include_router(v1_routers, prefix="/api/v1")


