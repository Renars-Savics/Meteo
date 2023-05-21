import scrapy

class WeatherItem(scrapy.Item):
    # punkts = scrapy.Field()
    pilseta = scrapy.Field()
    spiediens = scrapy.Field()
    temperatura = scrapy.Field()
    veja_atrums = scrapy.Field()
    veja_virziens = scrapy.Field()
    brazmas = scrapy.Field()
    nokrisni_1h = scrapy.Field()
    relativais_mitrums = scrapy.Field()
    sajutu_temperatura = scrapy.Field()
    sniegs = scrapy.Field()
    makoni = scrapy.Field()
    nokrisnu_varbutiba = scrapy.Field()
    uvi_indekss = scrapy.Field()

