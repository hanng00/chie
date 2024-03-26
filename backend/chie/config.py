import os

from dotenv import load_dotenv

if os.environ.get("APP_ENV") != "production":
    load_dotenv()


def _get_schemeless_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 54321 if host == "localhost" else os.getenv("DB_PORT", 5432)
    password = os.environ.get("DB_PASSWORD", "abc123")

    user = os.environ.get("DB_USER", "dummy_user")
    db_name = os.environ.get("DB_NAME", "postgres")

    return f"{user}:{password}@{host}:{port}/{db_name}"


def get_postgres_uri():
    schemeless_postgres_uri = _get_schemeless_postgres_uri()
    return f"postgresql://{schemeless_postgres_uri}"


def get_alembic_postgres_uri():
    schemeless_postgres_uri = _get_schemeless_postgres_uri()
    return f"postgresql+psycopg2://{schemeless_postgres_uri}"


def get_secret_jwt_key():
    return os.environ.get("JWT_SECRET_KEY")


def bypass_authentication():
    return os.environ.get("AUTHENTICATE", False)


def get_supabase_url_and_key():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY are required")

    return url, key


def get_uvicorn_config():
    is_development = os.getenv("APP_ENV", "development").lower() != "production"

    return {
        "host": os.getenv("HOST", "0.0.0.0"),
        "port": int(os.getenv("PORT", 8000)),
        "reload": is_development,
        "workers": 6,
    }
