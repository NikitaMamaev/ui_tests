# Запуск тестов
Тесты запускаются из корня проекта.

## Для Chrome:

```bash
sh ./test_chrome.sh
```

или

```bash
PYTHONPATH=${PWD} \
SELENIUM_BROWSER="chrome" \
SELENIUM_BROWSER_MODE="head" \
SELENIUM_BROWSER_LOCALE="en" \
pytest -v tests/*
```

## Для Firefox:

```bash
sh ./test_firefox.sh
```

или

```bash
PYTHONPATH=${PWD} \
SELENIUM_BROWSER="firefox" \
SELENIUM_BROWSER_MODE="head" \
SELENIUM_BROWSER_LOCALE="en" \
pytest -v tests/*
```

## Необходимые пакеты:

* `chromedriver`
* `geckodriver`
* `PyHamcrest`
* `pylint`
* `pytest`
* `requests`
* `selenium`
