"""
Browsers for tests and it's settings
"""

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Browser: #pylint: disable=too-few-public-methods
    """
    options: selenium class of browser options link
    options_arguments: list of browser options
    preferences: dict of browser options
    desired_capabilities: firefox dict of capabilities for browser
    desired_capabilities_arguments: capabilities for browser
    language: browser locale
    mode: browser mode
    """

    def __init__(self, name, options, **kwargs):
        self.name = name
        self.options = options()
        for argument in kwargs.get('options_arguments', []):
            self.options.add_argument(argument)
        for preference, value in kwargs.get('preferences', {}).items():
            self.options.set_preference(preference, value)
        self.options.headless = kwargs.get('mode') == "headless"

    @classmethod
    def _chrome(cls, locale, mode):
        return cls(name='Chrome',
                   options=ChromeOptions,
                   mode=mode,
                   options_arguments=[
                       '--disable-dev-shm-usage', # do not use shared memory
                       '--no-sandbox', # disable safety mode
                       '--ignore-certificate-errors', # to work with domains without certs
                       f'--lang={locale}',
                   ])

    @classmethod
    def _firefox(cls, locale, mode):
        lang = {
            'en': 'en_US',
            'ru': 'ru_RU',
        }.get(locale)
        return cls(name='Firefox',
                   options=FirefoxOptions,
                   mode=mode,
                   desired_capabilities=DesiredCapabilities.FIREFOX.copy(),
                   desired_capabilities_arguments={
                       'acceptInsecureCerts': True,
                       'acceptSslCerts': True,
                       'assume_untrusted_cert_issuer': True,
                   },
                   preferences={
                       'intl.accept_languages': lang,
                   })

    @classmethod
    def create(cls, name='Chrome', locale='en', mode='headless'):
        """
        Create browser  by name
        """

        return {'Chrome': cls._chrome(locale, mode),
                'Firefox': cls._firefox(locale, mode)}.get(name)
