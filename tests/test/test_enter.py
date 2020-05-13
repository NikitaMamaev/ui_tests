"""
Page enter test
"""

import hamcrest as hc

from src.pages.subscriptions import SubscriptionsPage


def test_enter(enter):
    """
    Try to enter the page
    """

    with SubscriptionsPage() as page:
        hc.assert_that(
            page.driver.current_url,
            hc.equal_to(page.url)
        )
