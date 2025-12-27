from scrapy.utils.project import get_project_settings
from sqlalchemy import Text, String
from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class News(Base):
    __tablename__ = "news"
    id = Column(Text, primary_key=True)
    fecha = Column("fecha", String(10))
    titulo = Column("titulo", String(100))
    subtitulo = Column("subtitulo", String(150))
    cuerpo = Column("cuerpo", Text)
    tags = Column("tags", String)
    url = Column("url", String(150))
    url_imagenes = Column("url_imagenes", String(150))
