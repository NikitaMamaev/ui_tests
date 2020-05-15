"""
Table clearing test
"""

import pytest

from src.pages.subscriptions import SubscriptionsPage
from tests.data.subscription import positive


@pytest.mark.deleting
@pytest.mark.positive
def test_deleting(enter):
    """
    Try to enter the page
    """

    with SubscriptionsPage() as page:
        page.input_data(positive)
        page.submit_button.click()
        page.clear_button.click()
        page.sync_button.click()
        page.table.wait_clearing()
