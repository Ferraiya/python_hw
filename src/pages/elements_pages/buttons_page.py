from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from config import BASE_URL

class ButtonsPage(BasePage):
    page_url = BASE_URL + "/buttons"
    button_double = (By.XPATH, '//button[@id="doubleClickBtn"]')
    message_double = (By.XPATH, '//*[@id="doubleClickMessage"]')
    button_right = (By.XPATH, '//button[@id="rightClickBtn"]')
    message_right = (By.XPATH, '//*[@id="rightClickMessage"]')
    button_dynamic = (By.XPATH, '//*[text()="Click Me"]')
    message_dynamic = (By.XPATH, '//*[@id="dynamicClickMessage"]')


    def __init__(self, driver):
        super().__init__(driver)


    def open(self):
        self.driver.get(self.page_url)

    def double_click(self):
        action = ActionChains(self.driver)
        self.wait_for_clickable(self.button_double)
        required_button = self.get_element(self.button_double)
        action.double_click(required_button).perform()
        self.wait_for(self.message_double)

    def right_click(self):
        action = ActionChains(self.driver)
        self.scroll_to_element(self.button_right)
        self.wait_for_clickable(self.button_right)
        right_button = self.get_element(self.button_right)
        action.context_click(right_button).perform()
        self.wait_for(self.message_right)