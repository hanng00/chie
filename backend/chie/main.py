import uvicorn
from fastapi import FastAPI
from chie.logger import get_logger
from chie.middleware.cors import add_cors_middleware

from chie.modules.mind.controllers.mind_routes import mind_router
from chie.modules.user.controllers.user_routes import user_router

from chie.config import get_uvicorn_config


def setup_fastapi_app():
    app = FastAPI()

    add_cors_middleware(app)

    app.include_router(mind_router, prefix="/mind", tags=["mind"])
    app.include_router(user_router, prefix="/user", tags=["user"])

    return app


logger = get_logger(__name__)
app = setup_fastapi_app()


def main():
    uvicorn_app = f"chie.main:app"
    uvicorn_config = get_uvicorn_config()

    uvicorn.run(uvicorn_app, **uvicorn_config)


if __name__ == "__main__":
    main()
