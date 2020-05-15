"""
Project settings
"""

from os import environ


LOCAL_IP = "192.168.0.3"

URL = f"http://{LOCAL_IP}:4000"

API_HANDLER = "/subscriptions"
UI_HANDLER = "/ui"

GITHUB_URL = "https://github.com/zeburek/flask-mongoengine-example"

LIST_LENGTH = 5

#
# Selenium settings
#
BROWSER = environ.get("SELENIUM_BROWSER", "Chrome").capitalize()
BROWSER_MODE = environ.get("SELENIUM_BROWSER_MODE", "headless")
BROWSER_LOCALE = environ.get("SELENIUM_BROWSER_LOCALE", "en")

#
# Browser window size
#
WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768

#
# Timeouts
#
DEFAULT_TIMEOUT = 10
PAGE_LOAD_TIMEOUT = 10
ELEMENT_CLICKABLE_TIMEOUT = 3
ELEMENT_APEARED_TIMEOUT = 3
ELEMENT_DISSAPEARED_TIMEOUT = 3
TABLE_CLEARING_TIMEOUT = 5
SUBSCRIPTION_APEARED_TIMEOUT = 5
