"""
Class for working with the subscriptions table
"""

import hamcrest as hc

from src.elements.element import Element
from src.misc.query import css_selector
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
        self.table_raw = Element(css_selector('tr[data-test="subs-table-row"]'))

    @property
    def data(self):
        """
        Subscriptions table parsing method
        """

        raws = self.table_raw.find_all()

        if not raws:
            return []

        table_data = []

        for raw in raws:
            active = None
            if self.indicator_success.find_all(parent=raw):
                active = True
            elif self.indicator_danger.find_all(parent=raw):
                active = False

            table_data.append({
                'email': self.email_cell.get_text(parent=raw),
                'name': self.name_cell.get_text(parent=raw),
                'active': active
            })

        return table_data

    def wait_clearing(self):
        """
        Wait for the table to clear
        """

        Wait(timeout=3).until(
            data=self.data,
            matcher=hc.empty(),
            message="Table has not cleared"
        )

    def wait_subscription(self, subscription: Subscription):
        """
        Wait for subscription to appear in table
        """

        Wait(timeout=3).until(
            data=self.data,
            matcher=hc.has_item(hc.has_entries({
                'email': subscription.email,
                'name': subscription.name
            })),
            message="Table has not cleared"
        )
