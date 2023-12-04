import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, RESULTS


DT_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_NAME = 'status_summary_{time}.csv'


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses_amount = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses_amount[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_path = self.results_dir / FILE_NAME.format(
            time=dt.now().strftime(DT_FORMAT)
        )
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows((
                ['Статус', 'Количество'],
                *self.statuses_amount.items(),
                ['Total', sum(self.statuses_amount.values())]
            ))
