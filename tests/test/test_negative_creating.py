"""
Tests of subscription creating with incorrect data
"""

import hamcrest as hc
import pytest

from src.pages.subscriptions import SubscriptionsPage
from tests.data.subscription import \
    empty_email, empty_name, empty_time, positive,\
    incorrect_email, incorrect_name, incorrect_time, zero_time


@pytest.mark.creating
@pytest.mark.negative
def test_creating_existing_subscription(enter, clean):
    """
    Try to create subscription with existing email
    """

    with SubscriptionsPage() as page:
        page.input_data(positive)
        page.submit_button.click()
        page.input_data(positive)
        page.submit_button.click()
        page.sync_button.click()
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.has_length(1),
            reason="Subscription with existing email should not be created!"
        )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_empty_email(enter, clean):
    """
    Try to create subscription with empty email
    """

    with SubscriptionsPage() as page:
        page.input_data(empty_email)
        page.submit_button.click()
        page.sync_button.click()
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.empty(),
            reason="Subscription with empty email should not be created!"
        )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_empty_name(enter, clean):
    """
    Try to create subscription with empty name
    """

    with SubscriptionsPage() as page:
        page.input_data(empty_name)
        page.submit_button.click()
        page.sync_button.click()
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.empty(),
            reason="Subscription with empty name should not be created!"
        )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_empty_time(enter, clean):
    """
    Try to create subscription with empty time
    """

    with SubscriptionsPage() as page:
        page.input_data(empty_time)
        page.submit_button.click()
        page.sync_button.click()
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.empty(),
            reason="Subscription with empty time should not be created!"
        )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_incorrect_email(enter, clean):
    """
    Try to create subscription with incorrect email
    """

    with SubscriptionsPage() as page:
        page.input_data(incorrect_email)
        page.submit_button.click()
        page.sync_button.click()
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.empty(),
            reason="Subscription with incorrect email should not be created!"
        )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_incorrect_name(enter, clean):
    """
    Try to create subscription with incorrect name
    """

    with SubscriptionsPage() as page:
        page.input_data(incorrect_name)
        page.submit_button.click()
        page.sync_button.click()
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.empty(),
            reason="Subscription with incorrect name should not be created!"
        )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_incorrect_time(enter, clean):
    """
    Try to create subscription with incorrect time
    """

    with SubscriptionsPage() as page:
        page.input_data(incorrect_time)
        page.submit_button.click()
        page.sync_button.click()
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.empty(),
            reason="Subscription with incorrect time should not be created!"
        )


@pytest.mark.creating
@pytest.mark.negative
def test_creating_with_zero_time(enter, clean):
    """
    Try to create subscription with zero time
    """

    with SubscriptionsPage() as page:
        page.input_data(zero_time)
        page.submit_button.click()
        page.sync_button.click()
        hc.assert_that(
            actual=page.table.data,
            matcher=hc.empty(),
            reason="Subscription with zero time should not be created!"
        )
