"""
Subscription page class description
"""

from src.elements.button import Button
from src.elements.field import Field
from src.elements.link import Link
from src.elements.subscriptions_table import SubscriptionsTable
from src.misc.query import css_selector
from src.pages.page import Page
import settings
from tests.data.subscription import Subscription


class SubscriptionsPage(Page):
    """
    Subscriptions page class
    """

    def __init__(self):
        super().__init__()
        self.url = f"{settings.URL}{settings.UI_HANDLER}"

        self.clear_button = Button(css_selector('button[data-test="clear-button"]'))
        self.email_field = Field(css_selector('input[data-test="new-subs-email"]'))
        self.github_link = Link(css_selector('a.nav-link'))
        self.name_field = Field(css_selector('input[data-test="new-subs-name"]'))
        self.submit_button = Button(css_selector('button[data-test="new-subs-submit"]'))
        self.sync_button = Button(css_selector('button[data-test="sync-button"]'))
        self.table = SubscriptionsTable()
        self.time_field = Field(css_selector('input[data-test="new-subs-time"]'))

    def input_data(self, data: Subscription):
        """
        Input test data in fields
        """

        self.email_field.input(data.email)
        self.name_field.input(data.name)
        self.time_field.input(data.time)
        