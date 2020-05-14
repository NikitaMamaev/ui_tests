"""
Wrapper on element localization methods
"""

from typing import NamedTuple

from selenium.webdriver.common.by import By


Locator = NamedTuple('Locator', [('method', By), ('query', str)])


def css_selector(query):
    """
    Localization with CSS SELECTOR
    """

    return Locator(method=By.CSS_SELECTOR, query=query)


def xpath(query):
    """
    Localization with XPATH
    """

    return Locator(method=By.XPATH, query=query)
