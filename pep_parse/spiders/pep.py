import re
import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        peps_href = response.css('#numerical-index td a::attr(href)')
        for pep_link in peps_href:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = re.search(
            r'PEP\s(?P<number>\d+)\W+(?P<name>.+)',
            response.css('h1.page-title::text').get()
        ).groups()
        data = {
            'number': number,
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)