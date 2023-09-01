from pathlib import Path

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

DOMAIN = 'peps.python.org'
URL = f'https://{DOMAIN}/'
PEP_PAGE_NUMBER_NAME_REGEX = r'PEP (?P<number>\d+) – (?P<name>.*)'
PEP_PAGE_STATUS_XPATH = ("//dl/*[contains(text(), 'Status')]"
                         "/following-sibling::dd/abbr/text()")
PEPS_PAGE_LIST_OF_URL_CSS = '#numerical-index table a::attr(href)'

BASE_DIR = Path(__file__).parent.parent
STATUS_SUMMARY_CSV_COLUMNS = ('Статус', 'Количество')

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
