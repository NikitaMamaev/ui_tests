export PYTHONPATH=${PWD}
export SELENIUM_BROWSER="firefox"
export SELENIUM_BROWSER_MODE="head"
export SELENIUM_BROWSER_LOCALE="en"

pytest -v tests/*
