import csv
from datetime import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR


RESULTS_DIR = 'results'
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_NAME = 'status_summary_{time}.csv'


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses_amount = defaultdict(int)
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.time = dt.now().strftime(DT_FORMAT)

    def process_item(self, item, spider):
        self.statuses_amount[item['status']] += 1
        return item

    def close_spider(self, spider):
        results = (
            ['Статус', 'Количество'],
            *self.statuses_amount.items(),
            ['Total', sum(self.statuses_amount.values())]
        )
        file_path = self.results_dir / FILE_NAME.format(time=self.time)
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(f, dialect=csv.unix_dialect).writerows(results)
