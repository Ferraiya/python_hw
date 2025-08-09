from src.pages.elements_pages.buttons_page import ButtonsPage

class TestButtons:

    def test_double_click(self, driver):
        buttons_page = ButtonsPage(driver)
        buttons_page.open()
        buttons_page.double_click()
        assert buttons_page.message_double

    def test_right_click(self, driver):
        buttons_page = ButtonsPage(driver)
        buttons_page.open()
        buttons_page.right_click()
        assert buttons_page.message_right

    def test_dynamic_click(self, driver):
        buttons_page = ButtonsPage(driver)
        buttons_page.open()
        buttons_page.click(buttons_page.button_dynamic)
        assert buttons_page.message_dynamic






