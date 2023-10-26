import scrapy


class QuotesSpider(scrapy.Spider):
    name = "primera_edicion"
    start_urls = ["https://www.primeraedicion.com.ar/?s=siniestro"]

    def parse(self, response):
        yield from response.follow_all(
            css="article div.jeg_postblock_content h3 a", callback=self.parse_news
        )

        pagination_links = response.css("li.next a")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_news(self, response):
        yield {
            "Titulo": response.css("div.entry-header h1 ::text").get(),
            "Subtitulo": response.css("div.entry-header h2 ::text").get(),
            "URL": response.url,
            "Fecha": response.css("div.entry-header div.jeg_meta_date a::text").get(),
            "Cuerpo": response.css(
                "div.entry-content div.content-inner p ::text"
            ).getall(),
            "Tags": response.css(
                "div.entry-content div.content-inner div.jeg_post_tags a::text"
            ).getall(),
            "Imajes": [
                img.attrib["data-src"]
                for img in response.css("div.jeg_inner_content img")
            ],
        }
