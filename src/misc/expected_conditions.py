"""
Conditions for waiters
"""


def element_is_appeared(element):
    """
    Check element is in browser
    """

    def check(parent):
        return bool(element.find_all(parent=parent))

    return check


def element_is_clickable(element):
    """
    Check that the element is clickable
    """
    def check(parent):

        if element.find_all(parent=parent):
            return element.find(parent=parent).is_enabled()

        return False

    return check


def element_is_disappeared(element):
    """
    Check element is not in browser
    """

    def check(parent):
        return not bool(element.find_all(parent=parent))

    return check


def page_state_is(state):
    """
    Check current page state
    """

    def check(driver):
        return driver.execute_script("return document.readyState") == state

    return check
