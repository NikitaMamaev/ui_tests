"""
Conditions for waiters
"""

def page_state_is(state):
    """
    Check current page state
    """

    def check(driver):
        return driver.execute_script("return document.readyState") == state

    return check
