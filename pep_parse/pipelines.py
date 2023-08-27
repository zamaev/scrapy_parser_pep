import csv
from collections import defaultdict
from datetime import datetime as dt
from pathlib import Path


BASE_DIR = Path('results')


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        now = dt.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = BASE_DIR / f'status_summary_{now}.csv'
        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Статус', 'Количество'))
            writer.writerows(self.status_count.items())
            writer.writerow(('Total', sum(self.status_count.values())))
