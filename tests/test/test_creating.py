"""
Page enter test
"""

import pytest

from src.pages.subscriptions import SubscriptionsPage
from tests.data.subscription import positive


@pytest.mark.creating
@pytest.mark.positive
def test_creating(enter):
    """
    Try to enter the page
    """

    with SubscriptionsPage() as page:
        page.input_data(positive)
        page.submit_button.click()
        page.sync_button.click()
        page.table.wait_subscription(positive)
        page.clear_button.click()
