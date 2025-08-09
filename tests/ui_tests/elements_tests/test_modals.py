from src.pages.elements_pages.modals_page import ModalsPage

class TestOpenModals:

    def test_open_small_modal(self, driver):
        modals_page = ModalsPage(driver)
        modals_page.open()

        modal = modals_page.click_button_small()
        assert modal.is_displayed()

        modals_page.close_small_modal()
        assert not driver.find_elements(*modals_page.small_modal)

    def test_open_large_modal(self, driver):
        modals_page = ModalsPage(driver)
        modals_page.open()

        modal = modals_page.click_button_large()
        assert modal.is_displayed()

        modals_page.close_large_modal()
        assert not driver.find_elements(*modals_page.large_modal)