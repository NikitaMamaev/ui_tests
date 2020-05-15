"""
Input field element class description
"""

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

        return field

    def input(self, value):
        """
        Set text if field
        """

        return self.clear().send_keys(value)
