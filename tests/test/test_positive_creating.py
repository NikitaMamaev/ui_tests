"""
Tests of subscription creating with correct data
"""

from time import sleep

import hamcrest as hc
import pytest

import settings
from src.pages.subscriptions import SubscriptionsPage
from tests.data.subscription import expiring_time, positive, small_time


@pytest.mark.creating
@pytest.mark.positive
def test_creating_with_correct_data(enter, clean):
    """
    Test of creating subscription with correct data
    """

    with SubscriptionsPage() as page:
        page.input_data(positive)
        page.submit_button.click()
        page.sync_button.click()
        page.table.wait_subscription(positive)


@pytest.mark.creating
@pytest.mark.positive
def test_creating_with_expiring_time(enter, clean):
    """
    Test of creating subscription with expiring time
    """

    with SubscriptionsPage() as page:
        page.input_data(expiring_time)
        page.submit_button.click()
        page.sync_button.click()
        page.table.wait_subscription(expiring_time)
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.has_item(hc.has_entries({
                'email': expiring_time.email,
                'name': expiring_time.name,
                'active': True
            })),
            reason="Supscription has expired!"
        )
        sleep(10)
        page.sync_button.click()
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.has_item(hc.has_entries({
                'email': expiring_time.email,
                'name': expiring_time.name,
                'active': False
            })),
            reason="Supscription has not expired!"
        )


@pytest.mark.creating
@pytest.mark.positive
def test_creating_with_small_time(enter, clean):
    """
    Test of creating subscription with correct data
    """

    with SubscriptionsPage() as page:
        page.input_data(small_time)
        page.submit_button.click()
        page.sync_button.click()
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.has_item(hc.has_entries({
                'active': True,
            })),
            reason="Supscription should be active!"
        )


@pytest.mark.creating
@pytest.mark.positive
def test_sixth_subscription_creating(fill_subscriptions_table):
    """
    Sixth subscription creating test
    """

    with SubscriptionsPage() as page:
        page.input_data(positive)
        page.submit_button.click()
        page.sync_button.click()
        page.table.wait_subscription(positive)

        hc.assert_that(
            actual=page.table.data,
            matcher=hc.not_(hc.has_item(hc.has_entries({
                'email': 'email1@example.com',
                'name': 'name1 lastname1',
            }))),
            reason="First subscription has not left the list"
        )

        hc.assert_that(
            actual=page.table.data,
            matcher=hc.has_length(settings.LIST_LENGTH),
            reason="Incorrect length of the list"
        )
