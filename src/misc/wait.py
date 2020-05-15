"""
Base class for waiters
"""

import time

import hamcrest as hc

import settings


class Wait:
    """
    Base class for waiters
    """

    def __init__(self, timeout=settings.DEFAULT_TIMEOUT, frequency=0.5):
        self.timeout = timeout
        self.frequency = frequency

    def until(self, data, matcher, message):
        """
        Check data matching while it returns True
        :param matcher: hamcrest matcher
        :param data: value to check
        :param message: message when timeout is reached
        """

        end_time = time.time() + self.timeout

        while time.time() < end_time:
            print(data)
            if matcher.matches(data):
                return

            time.sleep(self.frequency)

        hc.assert_that(actual=data, matcher=matcher, reason=message)
