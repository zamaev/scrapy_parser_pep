import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, STATUS_SUMMARY_CSV_COLUMNS


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        now = dt.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = BASE_DIR / f'results/status_summary_{now}.csv'
        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows([
                STATUS_SUMMARY_CSV_COLUMNS,
                *self.status_count.items(),
                ('Total', sum(self.status_count.values())),
            ])
