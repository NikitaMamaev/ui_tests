"""
Delete subscriptions before testing
"""

import pytest

from utils.api_requests import send_request


def delete_subscriptions() -> dict:
    """
    Delete all subscriptions
    """

    response = send_request(
        method='delete'
    )

    return response


@pytest.fixture(scope='session')
def clean(request):
    """
    Delete subscriptions if the list is not empty
    """

    if send_request():
        delete_subscriptions()

    request.addfinalizer(delete_subscriptions)
