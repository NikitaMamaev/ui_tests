"""
Subscription data for tests
"""

from dataclasses import dataclass


@dataclass
class Subscription:
    """
    Subscription parameters
    """

    email: str = ""
    name: str = ""
    time: str = "1d"


empty_email = Subscription(
    email="",
    name="Empty Email"
)

empty_name = Subscription(
    email="empty_name@example.com",
    name=""
)

empty_time = Subscription(
    email="empty_time@example.com",
    name="Empty Time",
    time=""
)

expiring_time = Subscription(
    email="expiring_time@example.com",
    name="Expiring Time",
    time="8h5s"
)

incorrect_email = Subscription(
    email="incorrect_email",
    name="Incorrect Email"
)

incorrect_name = Subscription(
    email="incorrect_name@example.com",
    name="./*#@!%|^&*(),'`~;:+-}_=[]?\"<>{",
    time="incorrect name"
)

incorrect_time = Subscription(
    email="incorrect_time@example.com",
    name="Incorrect Time",
    time="incorrect time"
)

positive = Subscription(
    email="positive@example.com",
    name="Positive Name"
)

small_time = Subscription(
    email="small_time@example.com",
    name="Small Time",
    time="2h"
)

xss_name = Subscription(
    email="xss_name@example.com",
    name="<script>alert('xss');</script>"
)

zero_time = Subscription(
    email="zero_time@example.com",
    name="Zero Time",
    time="0d"
)
