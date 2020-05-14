"""
Base class for page elements
"""

from selenium.webdriver.support.wait import WebDriverWait

from src.misc.driver import Driver
from src.misc.query import Locator
from src.misc.expected_conditions import element_is_appeared, element_is_disappeared


class Element:
    """
    Base page element which has locator and can be found
    """

    def __init__(self, locator: Locator):
        self.driver = Driver()
        self.locator = locator

    def get_attribute(self, attr):
        """
        Get value of element's attribute
        """

        return self.find().get_attribute(attr)

    def find_all(self):
        """
        Search for all elements by locator
        """

        return self.driver.find_elements(*self.locator)

    def find(self, timeout=15):
        """
        Search for the first element by locator
        """

        self.wait(timeout=timeout)
        elements = self.find_all()
        if elements:
            return elements[0]

        return None

    def wait(self, timeout=30):
        """
        Wait for the element to appear
        """

        WebDriverWait(self.driver, timeout).until(element_is_appeared(self))

        return self

    def wait_is_disappeared(self, timeout=30):
        """
        Wait for the element to disappear
        """

        WebDriverWait(self.driver, timeout).until(element_is_disappeared(self))

        return self

    def click(self):
        """
        Click on element
        """
        element = self.find()
        if element:
            element.click()

        return self
