"""
Delete subscriptions after testing
"""

import pytest

from src.pages.subscriptions import SubscriptionsPage


@pytest.fixture(scope='function')
def clean(request):
    """
    Delete subscriptions after testing
    """

    request.addfinalizer(SubscriptionsPage().clear_button.click)
