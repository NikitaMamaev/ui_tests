export PYTHONPATH=${PWD}
export DEBUG_MODE=True
export SELENIUM_BROWSER="chrome"
export SELENIUM_BROWSER_MODE="head"
export SELENIUM_BROWSER_LOCALE="en"

pytest -v tests/*
