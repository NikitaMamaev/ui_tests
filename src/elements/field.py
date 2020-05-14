"""
Input field element class description
"""

from selenium.webdriver.common.keys import Keys

from src.elements.element import Element


class Field(Element):
    """
    Class for input fields
    """

    def clear(self):
        """
        Clear field
        """

        field = self.find()
        field.clear()

        if self.get_attribute("value"):
            field.send_keys(Keys.END)
            field.send_keys(Keys.SHIFT, Keys.HOME)
            field.send_keys(Keys.DELETE)

        return field

    def input(self, value):
        """
        Set text if field
        """

        return self.clear().send_keys(value)
