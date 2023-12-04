# Парсер документов PEP на базе фреймворка Scrapy
* Автор: [Федор Абаза](https://github.com/thedross)
## Описание
Парсер собирает информацию о PEP и сохраняет её в два файла:

* pep_.css  --  номер, название и статус каждого PEP.
* status_summary__.css -- название и подсчет количества всех статусов PEP.

### Стек технологий:
```
* Python 3

* Scrapy
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/thedross/bs4_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустить парсер:

```
scrapy crawl pep
```
