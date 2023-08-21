import scrapy

class SpiderFerramentas(scrapy.Spider):
    name = 'ferramentas'

    start_urls = ['https://pt.stardewvalleywiki.com/Ferramentas']

    def parse(self, response):
        nomes = []
        precos = []

        for i in response.css('td+ td:nth-child(2) a::text').getall():
            nomes.append(i)

        for i in response.css('.no-wrap::text').getall():
            precos.append(i.replace('\xa0', ''))

        for i, j in zip(nomes, precos):
            yield {
                'nome': i,
                'preco': j
            }
