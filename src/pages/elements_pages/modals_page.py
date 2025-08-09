from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import BASE_URL


class ModalsPage(BasePage):
    page_url = BASE_URL + "/modal-dialogs"
    button_small = (By.XPATH, '//*[@id="showSmallModal"]')
    button_large = (By.XPATH, '//*[@id="showLargeModal"]')
    small_modal = (By.XPATH, '//*[@id="example-modal-sizes-title-sm"]')
    large_modal = (By.XPATH, '//*[@id="example-modal-sizes-title-lg"]')
    button_close_small = (By.XPATH, '//*[@id="closeSmallModal"]')
    button_close_large = (By.XPATH, '//*[@id="closeLargeModal"]')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.page_url)

    def click_button_small(self):
        self.wait_for_clickable(self.button_small)
        self.get_element(self.button_small).click()
        modal = (self.get_element(self.small_modal))
        self.wait_for(self.small_modal)
        return modal

    def click_button_large(self):
        self.wait_for_clickable(self.button_large)
        self.get_element(self.button_large).click()
        modal = (self.get_element(self.large_modal))
        self.wait_for(self.large_modal)
        return modal

    def close_small_modal(self):
        modal = (self.get_element(self.small_modal))
        self.wait_for_clickable(self.button_small)
        self.get_element(self.button_close_small).click()
        self.wait_disappear(self.small_modal)
        return modal

    def close_large_modal(self):
        modal = (self.get_element(self.large_modal))
        self.wait_for_clickable(self.button_large)
        self.get_element(self.button_close_large).click()
        self.wait_disappear(self.large_modal)
        return modal



