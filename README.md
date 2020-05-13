# Запуск тестов
Тесты запускаются из корня проекта:

```bash
sh ./test.sh
```

или

```bash
PYTHONPATH=${PWD} \
DEBUG_MODE=True \
SELENIUM_BROWSER="chrome" \
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
