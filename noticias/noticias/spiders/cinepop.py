import scrapy
from noticias.items import NoticiasItem

class CinepopSpider(scrapy.Spider):
    name = 'cinepop'
    allowed_domains = ['cinepop.com.br']
    start_urls = ['http://cinepop.com.br/']

    def parse(self, response):

        for link in response.css("div.td-module-thumb a::attr(href)").getall():

            yield response.follow(link, self.parse_article)


    def parse_article(self, response):

        title = response.css("h1.entry-title::text").get()
        author = response.css("div.td-post-author-name a::text").get()
        date = response.css("span.td-post-date time::text").get()
        text = "".join(response.css("div.td-post-content.tagdiv-type p::text").getall())
        link = response.url
        tags = response.css("div.td-post-source-tags li a::text").getall()

        # Métricas
        quantTags = len(tags)
        time = str(self.tempoDeLeitura(text)) + " min de leitura"

        dados = NoticiasItem(title=title, author=author, date=date, text=text, link=link, time=time, tags=tags, quantTags=quantTags)
        yield dados


    def tempoDeLeitura(self, text):
        # Estipula-se que o tempo medio para leitura de cada palavra é em torno de 0.39 s
        # Portanto:

        palavras = text.split()

        quantPalavras = len(palavras)
        tempoSegundos = float(quantPalavras * 0.39)
        tempoMinutos = int(tempoSegundos / 60.0)

        return tempoMinutos