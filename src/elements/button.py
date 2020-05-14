"""
Button element class description
"""

from selenium.webdriver.support.wait import WebDriverWait

from src.elements.element import Element
from src.misc.expected_conditions import element_is_clickable


class Button(Element):
    """
    Class for buttons
    """

    def click(self):
        """
        Click button after it becomes clickable
        """

        self.wait_is_clickable()
        button = self.find()
        if button:
            button.click()

        return self

    def wait_is_clickable(self, timeout=30):
        """
        Wait until the button is clickable
        """

        WebDriverWait(self.driver, timeout).until(element_is_clickable(self))

        return self
