import os
import uvicorn
from fastapi import FastAPI
from chie.middleware.cors import add_cors_middleware
from chie.mind.controllers.mind_routes import mind_router
from dotenv import load_dotenv

app = FastAPI()

add_cors_middleware(app)

app.include_router(mind_router, prefix="/mind", tags=["mind"])


def main():
    is_development = os.getenv("APP_ENV", "development").lower() != "production"
    if is_development:
        load_dotenv()

    uvicorn_app = f"chie.main:app"

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    reload = is_development

    uvicorn.run(uvicorn_app, host=host, port=port, reload=reload)

if __name__ == "__main__":
    main()