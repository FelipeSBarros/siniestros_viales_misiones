# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import uuid
from datetime import datetime

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker

from scraping_siniestros_viales.models import News, create_table, db_connect

MESES = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12,
}


class ScrapingSiniestrosVialesPipeline:
    def process_item(self, item, spider):
        # if item is None:
        #     raise DropItem("Item None descartado")
        adapter = ItemAdapter(item)
        url = adapter.get("url")
        id = uuid.uuid5(uuid.NAMESPACE_URL, url)
        adapter["id"] = str(id)
        return item


class ValidacionFechaPipeline:
    fecha_inicial = datetime(2023, 12, 31).date()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        fecha_str = adapter.get("fecha")
        dia, mes, ano = fecha_str.split()

        mes = MESES.get(mes.lower().strip(","))
        fecha = datetime(int(ano), mes, int(dia)).date()
        if fecha < spider.fecha_inicial:
            raise DropItem("Fecha de la notícia es anterior a la fecha deseada")
        else:
            adapter["fecha"] = fecha
            return item


class SaveNewsPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        news_table = News()
        adapter = ItemAdapter(item)

        news_table.id = adapter.get("id")
        news_table.fecha = adapter.get("fecha")
        news_table.titulo = adapter.get("titulo")
        news_table.subtitulo = adapter.get("subtitulo")
        news_table.cuerpo = adapter.get("cuerpo")
        news_table.tags = adapter.get("tags")
        news_table.url = adapter.get("url")
        news_table.url_imagenes = adapter.get("url_imagenes")

        try:
            session.add(news_table)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()


class DuplicateNewsPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates tables.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        adapter = ItemAdapter(item)
        id_scrapped = adapter.get("id")
        exist_new = session.query(News).filter_by(id=id_scrapped).first()
        session.close()
        if exist_new:  # the current quote exists
            raise DropItem("Duplicate item found: %s" % item["id"])
        else:
            return item
