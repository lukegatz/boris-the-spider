import scrapy

'''
A classe WeatherForescastSpider estende Spider e é responsável por navegar pela(s) página(s) estabelecida(s), 
buscando as informações sobre o clima que queremos retornar (temperatura, nome das estações de medição.
'''
class WeatherForecastSpider(scrapy.Spider):
    # o nome do spider (que pode ser acessado por meio de scrapy crawl [name])
    name = 'weather-forecast'
    # o domínio relacionado ao spider que estamos executando
    allowed_domains = ['www.weather-forecast.com']
    # as urls em que o spider iniciará sua navegação
    start_urls = [
        'https://www.weather-forecast.com/locations/Sao-Paulo-Congonhas-Airport/forecasts/latest/',
    'https://www.weather-forecast.com/locations/Sao_Paulo_Guarulhos_International_Airport/forecasts/latest'
    ]

    '''
    O método parse é o responsável por retornar os dados de 'estação' e 'temperatura' que estamos buscando
    por meio do spider.
    '''
    def parse(self, response):
        return {
            "estação": response.xpath('//h2/text()').extract_first(),
            "temperaturas": response.xpath('//div/span[@class="temp"]/text()').getall()
        }
