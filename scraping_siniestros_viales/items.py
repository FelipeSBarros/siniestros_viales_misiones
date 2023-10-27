import scrapy
from itemloaders.processors import MapCompose, Join, TakeFirst


class NewsItem(scrapy.Item):
    titulo = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=TakeFirst())
    subtitulo = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=TakeFirst())
    url = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=TakeFirst())
    fecha = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=TakeFirst())
    cuerpo = scrapy.Field(input_processor=MapCompose(str.strip),
                          output_processor=Join())
    tags = scrapy.Field(input_processor=MapCompose(str.strip),
                        output_processor=Join(","))
    url_imagenes = scrapy.Field(input_processor=MapCompose(str.strip),
                                output_processor=TakeFirst())
