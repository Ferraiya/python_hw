from src.pages.browser import Browser


class Element(object):

    def __init__(self, locator):
        self.locator = locator
        self.browser = Browser()

    def set_value(self, value):
        elem = self.browser.get_element(self.locator)
        self.browser.wait_for_clickable(self.locator)
        elem.send_keys(value)
        return self

