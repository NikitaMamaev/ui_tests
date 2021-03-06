"""
Base class for page elements
"""

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

import settings
from src.misc.driver import Driver
from src.misc.query import Locator
from src.misc.expected_conditions import element_is_appeared, element_is_disappeared


class Element:
    """
    Class for base page element which has locator and can be found
    """

    def __init__(self, locator: Locator):
        self.driver = Driver()
        self.locator = locator

    def get_text(self, parent: WebElement = None):
        """
        Get text from element
        """

        element = self.find(parent=parent)
        if element:
            return element.text

        return ""

    def find_all(self, parent: WebElement = None):
        """
        Search for all elements by locator
        """
        if not parent:
            parent = self.driver

        return self.driver.find_elements(*self.locator)

    def find(self, parent: WebElement = None, timeout=settings.ELEMENT_APEARED_TIMEOUT):
        """
        Search for the first element by locator
        """

        self.wait(parent=parent, timeout=timeout)
        elements = self.find_all(parent=parent)
        if elements:
            return elements[0]

        return None

    def wait(self, parent: WebElement = None, timeout=settings.ELEMENT_APEARED_TIMEOUT):
        """
        Wait for the element to appear
        """

        WebDriverWait(parent, timeout).until(element_is_appeared(self))

        return self

    def wait_is_disappeared(self, timeout=settings.ELEMENT_DISSAPEARED_TIMEOUT):
        """
        Wait for the element to disappear
        """

        WebDriverWait(self.driver, timeout).until(element_is_disappeared(self))

        return self
