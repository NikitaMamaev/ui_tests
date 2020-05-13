"""
Project settings
"""

from os import environ


LOCAL_IP = "192.168.0.3"

URL = f"http://{LOCAL_IP}:4000"

API_HANDLER = "/subscriptions"
UI_HANDLER = "/ui"

DEBUG_MODE = environ.get("DEBUG", False)

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
PAGE_LOAD_TIMEOUT = 5
