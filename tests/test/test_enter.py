"""
Page enter test
"""

from time import sleep

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

        sleep(5)
        hc.assert_that(
            page.driver.current_url,
            hc.equal_to(page.url)
        )
