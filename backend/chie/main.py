import os
import uvicorn
from fastapi import FastAPI
from chie.logger import get_logger
from chie.middleware.cors import add_cors_middleware
from dotenv import load_dotenv

from chie.modules.mind.controllers.mind_routes import mind_router
from chie.modules.user.controllers.user_routes import user_router

logger = get_logger(__name__)

app = FastAPI()

add_cors_middleware(app)

app.include_router(mind_router, prefix="/mind", tags=["mind"])
app.include_router(user_router, prefix="/user", tags=["user"])


def main():
    is_development = os.getenv("APP_ENV", "development").lower() != "production"
    if is_development:
        logger.info("Running in DEVELOPMENT mode")
        load_dotenv()

    uvicorn_app = f"chie.main:app"

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    reload = is_development

    uvicorn.run(uvicorn_app, host=host, port=port, reload=reload)


if __name__ == "__main__":
    main()
