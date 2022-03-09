import scrapy
from noticias.items import NoticiasItem

class OmeleteSpider(scrapy.Spider):
    name = 'omelete'
    allowed_domains = ['www.omelete.com.br']
    start_urls = ['http://www.omelete.com.br/']

    def parse(self, response):
        for link in response.css("main.c-newslist article div a::attr(href)").getall():

            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        title = response.css("div.article__header__title h1::text").get()
        author = response.css("div.info__by::text").get()
        date = response.css("div.info__date::text").get()
        text = "".join(response.css("div.article__body.article--content ::text").getall())
        link = response.url
        time =response.css("div.reading-time__text::text").get()

        dados = NoticiasItem(title=title, author=author, date=date, text=text, link=link, time=time)
        yield dados

