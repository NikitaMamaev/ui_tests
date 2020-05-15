"""
Base class for pages
"""

from selenium.webdriver.support.expected_conditions import url_matches
from selenium.webdriver.support.wait import WebDriverWait

from src.misc.expected_conditions import page_state_is
from src.misc.driver import Driver
import settings


class Page:
    """
    Base class for pages
    """

    def __init__(self):
        self.driver = Driver()
        self.url = ""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def open(self, timeout: int = settings.PAGE_LOAD_TIMEOUT):
        """
        Open the page by url
        """

        self.driver.get(self.url)
        self.wait(timeout=timeout)

    def wait(self, timeout: int = settings.PAGE_LOAD_TIMEOUT):
        """
        Wait page opening
        """

        WebDriverWait(self.driver, timeout).until(
            url_matches(self.url)
        )
        WebDriverWait(self.driver, timeout).until(
            page_state_is('complete')
        )
        