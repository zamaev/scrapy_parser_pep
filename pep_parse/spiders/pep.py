import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import (DOMAIN, PEP_PAGE_NUMBER_NAME_REGEX,
                                PEP_PAGE_STATUS_XPATH,
                                PEPS_PAGE_LIST_OF_URL_CSS, URL)


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [DOMAIN]
    start_urls = [URL]

    def parse(self, response):
        all_peps = response.css(PEPS_PAGE_LIST_OF_URL_CSS).getall()
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        header = response.css('h1.page-title::text').get()
        number, name = re.search(
            PEP_PAGE_NUMBER_NAME_REGEX,
            header,
        ).groups()
        status = response.xpath(PEP_PAGE_STATUS_XPATH).get()
        yield PepParseItem(
            number=number,
            name=name,
            status=status,
        )
