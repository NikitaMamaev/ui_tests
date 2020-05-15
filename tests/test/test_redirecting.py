"""
Page enter test
"""

import pytest

from src.pages.github import GithubPage
from src.pages.subscriptions import SubscriptionsPage


@pytest.mark.positive
@pytest.mark.redirecding
def test_redirecting(enter):
    """
    Try to enter the page
    """

    with SubscriptionsPage() as page:
        page.github_link.click()

        with GithubPage() as github:
            github.wait()

        page.open()
