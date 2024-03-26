from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
from chie.config import get_postgres_uri
from sqlalchemy import MetaData

engine = create_engine(get_postgres_uri())

Base = declarative_base()

# Import Models defined in other files
relative_paths = [
    "chie.models.mind",
]


def import_models():
    for path in relative_paths:
        __import__(path, globals(), locals())


import_models()
