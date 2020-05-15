export PYTHONPATH=${PWD}
export SELENIUM_BROWSER="firefox"
export SELENIUM_BROWSER_MODE="head" # or "headless"
export SELENIUM_BROWSER_LOCALE="en"

pytest -v tests/*
