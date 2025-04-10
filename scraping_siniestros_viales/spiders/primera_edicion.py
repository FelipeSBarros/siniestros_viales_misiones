import scrapy
from scrapy.loader import ItemLoader

from scraping_siniestros_viales.items import NewsItem


class SiniestrosVialesSpider(scrapy.Spider):
    name = "primera_edicion"
    start_urls = [
        f"https://www.primeraedicion.com.ar/page/{i}/?s=siniestro"
        for i in range(2, 197)
    ]
    start_urls.insert(0, "https://www.primeraedicion.com.ar/?s=siniestro")

    def parse(self, response):
        yield from response.follow_all(
            css="article div.jeg_postblock_content h3 a", callback=self.parse_news
        )

        pagination_links = response.css("li.next a")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_news(self, response):
        loader = ItemLoader(item=NewsItem(), selector=response)
        loader.add_css("titulo", "div.entry-header h1 ::text")
        loader.add_css("subtitulo", "div.entry-header h2 ::text")
        loader.add_value("url", response.url)
        loader.add_css("fecha", "div.entry-header div.jeg_meta_date a::text")
        loader.add_css("cuerpo", "div.entry-content div.content-inner p ::text")
        loader.add_css(
            "tags", "div.entry-content div.content-inner div.jeg_post_tags a::text"
        )
        loader.add_value(
            "url_imagenes",
            [
                img.attrib["data-src"]
                for img in response.css("div.jeg_inner_content img")
            ],
        )
        yield loader.load_item()
