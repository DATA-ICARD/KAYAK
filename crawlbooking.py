import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import HotelBookingItem


class CrawlbookingSpider(CrawlSpider):
    name = 'crawlbooking'
    allowed_domains = ['booking.com']
    start_urls = ['https://www.booking.com/searchresults.fr.html?aid=304142&ss=Mont=Saint=Michel&nflt=ht_id%3D204',
'https://www.booking.com/searchresults.fr.html?aid=304142&ss=St=Malo&nflt=ht_id%3D204',
'https://www.booking.com/searchresults.fr.html?aid=304142&ss=Bayeux&nflt=ht_id%3D204',
'https://www.booking.com/searchresults.fr.html?aid=304142&ss=Le+Havre&nflt=ht_id%3D204',
'https://www.booking.com/searchresults.fr.html?aid=304142&ss=Rouen&nflt=ht_id%3D204]',
'https://www.booking.com/searchresults.fr.html?aid=304142&ss=Paris&nflt=ht_id%3D204]',
'https://www.booking.com/searchresults.fr.html?aid=304142&ss=Amiens&nflt=ht_id%3D204]',
'https://www.booking.com/searchresults.fr.html?aid=304142&ss=Lille&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Strasbourg&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Chateau+du+Haut+Koenigsbourg&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Colmar&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Eguisheim&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Besancon&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Dijon&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Annecy&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Grenoble&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Lyon&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Gorges+du+Verdon&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Bormes+les+Mimosas&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Cassis&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Marseille&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Aix+en+Provence&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Avignon&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Uzes&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Nimes&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Aigues+Mortes&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Saintes+Maries+de+la+mer&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Collioure&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Carcassonne&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Ariege&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Toulouse&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Montauban&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Biarritz&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=Bayonne&nflt=ht_id%3D204]',
'[https://www.booking.com/searchresults.fr.html?aid=304142&ss=La+Rochelle&nflt=ht_id%3D204]']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942"]'), callback='parse_item', follow=True),
    ) #url

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True, meta={'start_url': url})
            
    def parse_item(self, response):
        ld_json = response.xpath('//script[@type="application/ld+json"]//text()').get()
        
        
        yield {
        'ld_json':ld_json 
        }
        
