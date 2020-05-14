"""
Subscription page class description
"""

from selenium.webdriver.support.expected_conditions import url_matches
from selenium.webdriver.support.wait import WebDriverWait

from src.elements.button import Button
from src.elements.field import Field
from src.misc.expected_conditions import page_state_is
from src.misc.driver import Driver
from src.misc.query import css_selector
import settings
from tests.data.subscription import Subscription


class SubscriptionsPage:
    """
    Subscriptions page class
    """

    def __init__(self):
        self.driver = Driver()
        self.url = f"{settings.URL}{settings.UI_HANDLER}"

        self.submit_button = Button(css_selector('button[data-test="new-subs-submit"]'))
        self.email_field = Field(css_selector('input[data-test="new-subs-email"]'))
        self.name_field = Field(css_selector('input[data-test="new-subs-name"]'))
        self.time_field = Field(css_selector('input[data-test="new-subs-time"]'))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def input_data(self, data: Subscription):
        """
        Input test data in fields
        """

        self.email_field.input(data.email)
        self.name_field.input(data.name)
        self.time_field.input(data.time)


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
        