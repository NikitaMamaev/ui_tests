"""
Page enter test
"""

import hamcrest as hc

from src.pages.subscriptions import SubscriptionsPage
from tests.data.subscription import positive


def test_enter(enter):
    """
    Try to enter the page
    """

    with SubscriptionsPage() as page:
        page.input_data(positive)
        page.submit_button.click()
        page.table.wait_subscription(positive)

        hc.assert_that(
            actual=page.table.data,
            matcher=hc.not_(hc.empty()),
            reason="Subscriptions table is empty!"
        )

        hc.assert_that(
            actual=page.table.data,
            matcher=hc.has_items(hc.has_entries({
                'email': positive.email,
                'name': positive.name,
                'active': False
            })),
            reason="There is no new subscription in the table!"
        )
