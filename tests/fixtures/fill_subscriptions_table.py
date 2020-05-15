"""
Fill the subscriptions list
"""

import hamcrest as hc
import pytest

import settings
from src.pages.subscriptions import SubscriptionsPage
from tests.data.subscription import Subscription


@pytest.fixture(scope='function')
def fill_subscriptions_table(request, enter):
    """
    Create five subscriptions before testing
    """

    with SubscriptionsPage() as page:
        for index in range(settings.LIST_LENGTH):
            page.input_data(
                data=Subscription(
                    email=f"email{index+1}@example.com",
                    name=f"name{index+1} lastname{index+1}"
                )
            )
            page.submit_button.click()

        page.sync_button.click()
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.has_length(settings.LIST_LENGTH),
            reason="The list is not full"
        )

    request.addfinalizer(SubscriptionsPage().clear_button.click)
