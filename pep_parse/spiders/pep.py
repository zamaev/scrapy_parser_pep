import re

import scrapy

from pep_parse.items import PepParseItem

DOMAIN = 'peps.python.org'
URL = f'https://{DOMAIN}/'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [DOMAIN]
    start_urls = [URL]

    def parse(self, response):
        all_peps = response.css(
            '#numerical-index table a::attr(href)').getall()
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        header = response.css('h1.page-title::text').get()
        number, name = re.search(
            r'PEP (?P<number>\d+) – (?P<name>.*)',
            header,
        ).groups()
        status = response.xpath("//dl/*[contains(text(), 'Status')]"
                                "/following-sibling::dd/abbr/text()").get()
        yield PepParseItem(
            number=number,
            name=name,
            status=status,
        )
