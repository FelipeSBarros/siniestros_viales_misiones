from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "primera_edicion"
    start_urls = ['https://www.primeraedicion.com.ar/?s=siniestro']

    def parse(self, response):
        for card in response.css('article div.jeg_postblock_content'):
            yield {
                "Titulo": card.css('h3 ::text').getall(),
                "URL": card.css('h3 a::attr(href)').getall(),
                "Fecha": card.css("div.jeg_post_meta div.jeg_meta_date a ::text").get(),
            }
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")