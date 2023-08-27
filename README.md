# scrapy_parser_pep

Парсер документов PEP на странице https://peps.python.org/.

На выходе парсер создает два файла:
- **pep_ДатаВремя.csv** со списком всех PEP со статусами
- **status_summary_ДатаВремя.csv** с количество PEP в каждом статусе и суммарным количеством PEP


## Запуск проекта
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:zamaev/scrapy_parser_pep.git
cd scrapy_parser_pep
```

Установить и активировать виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```


## Запуск парсера
Для получения актуальных данных с сайта нужно запустить парсер:
```bash
scrapy crawl pep
```


## Авторы
- [Айдрус](https://github.com/zamaev)
