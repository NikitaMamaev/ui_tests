"""
Subscription page class description
"""

from src.pages.page import Page
import settings


class GithubPage(Page):
    """
    Subscriptions page class
    """

    def __init__(self):
        super().__init__()
        self.url = settings.GITHUB_URL
        