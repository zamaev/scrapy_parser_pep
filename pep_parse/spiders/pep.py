import re
import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

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
