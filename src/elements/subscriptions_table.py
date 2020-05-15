"""
Class for working with the subscriptions table
"""

import hamcrest as hc

import settings
from src.elements.element import Element
from src.misc.query import css_selector, xpath
from src.misc.wait import Wait
from tests.data.subscription import Subscription


class SubscriptionsTable:
    """
    Subscriptions table class
    """

    def __init__(self):
        self.email_cell = Element(css_selector('[data-test="subs-table-email"]'))
        self.indicator_danger = Element(css_selector('svg.text-danger'))
        self.indicator_success = Element(css_selector('svg.text-success'))
        self.name_cell = Element(css_selector('[data-test="subs-table-name"]'))
        self.table_row = Element(xpath("//tbody//tr[@data-test='subs-table-row']"))

    @property
    def _rows(self):
        return self.table_row.find_all()

    @property
    def data(self):
        """
        Subscriptions table parsing method
        """

        if not self._rows:
            return []

        table_data = []

        for row in self._rows:
            active = None
            email = self.email_cell.get_text(parent=row)
            name = self.name_cell.get_text(parent=row)

            if self.indicator_success.find_all(parent=row):
                active = True
            elif self.indicator_danger.find_all(parent=row):
                active = False

            table_data.append({
                'email': email,
                'name': name,
                'active': active
            })

        return table_data

    def wait_clearing(self):
        """
        Wait for the table to clear
        """

        Wait(timeout=settings.TABLE_CLEARING_TIMEOUT).until(
            data=self._rows,
            matcher=hc.empty(),
            message="Table has not cleared!"
        )

    def wait_subscription(self, subscription: Subscription):
        """
        Wait for subscription to appear in table
        """

        Wait(timeout=settings.SUBSCRIPTION_APEARED_TIMEOUT).until(
            data=self.data,
            matcher=hc.has_item(hc.has_entries({
                'email': subscription.email,
                'name': subscription.name
            })),
            message="There is no new subscription in the table!"
        )
