# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import uuid
from datetime import datetime

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

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
