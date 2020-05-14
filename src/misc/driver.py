"""
Selenium driver
"""

from selenium import webdriver

import settings
from src.misc.browser import Browser


class Driver:
    """
    Selenium driver as singletone
    """

    class DriverHelper:
        """
        Subclass for driver creating
        """

        driver = None

        @classmethod
        def create(cls):
            """
            Create selenium driver
            """

            result = cls()

            browser = Browser.create(
                name=settings.BROWSER,
                locale=settings.BROWSER_LOCALE,
                mode=settings.BROWSER_MODE
            )

            BrowserClass = getattr(webdriver, browser.name) #pylint: disable=invalid-name
            result.driver = BrowserClass(options=browser.options)
            result.driver.set_window_size(
                width=settings.WINDOW_WIDTH,
                height=settings.WINDOW_HEIGHT
            )

            return result

    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = cls.DriverHelper.create()
        return cls.__instance.driver
