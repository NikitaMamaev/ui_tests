

import pytest

from src.misc.driver import Driver
from src.pages.subscriptions import SubscriptionsPage


def escape():
    """
    Close browser
    """

    Driver().quit()


@pytest.fixture(scope='session')
def enter(request, clean):
    """
    Open browser
    """

    with SubscriptionsPage() as page:
        page.open()

    request.addfinalizer(escape)
