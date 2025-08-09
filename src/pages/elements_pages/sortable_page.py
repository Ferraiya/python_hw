from selenium.webdriver import ActionChains
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import BASE_URL
from time import sleep

class SortablePage(BasePage):
    page_url = BASE_URL + "/sortable"
    line_elements = (By.XPATH, '//*[@id="demo-tabpane-list"]/div/div')
    grid_elements = (By.XPATH, '//*[@id="demo-tabpane-grid"]/div/div')
    list_tab_selector = (By.XPATH, '//*[@id="demo-tab-list"]')
    grid = (By.XPATH, '//*[@id="demo-tab-grid"]')
    grid_active = (By.XPATH, '//*[@id="demo-tabpane-grid" and contains(@class, "active")]')
    source = (By.CSS_SELECTOR, '#demo-tabpane-list > div > div:nth-child(5)')
    target = (By.CSS_SELECTOR, '#demo-tabpane-list > div > div:nth-child(2)')
    source_grid = (By.XPATH, '//*[@id="demo-tabpane-grid"]/div/div/div[5]')
    target_grid = (By.XPATH, '//*[@id="demo-tabpane-grid"]/div/div/div[9]')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.page_url)

    def grid_click(self):
        self.get_element(self.grid).click()
        self.wait_for(self.grid_active)

    def content_of_items(self, driver):
        self.wait_for(self.line_elements)
        driver.execute_script("window.scrollBy(0, 300);")
        elements = self.find_all(self.line_elements)
        return [el.text for el in elements]

    def content_of_grid_items(self, driver):
        self.wait_for(self.grid_elements)
        elements = self.find_all(self.grid_elements)
        driver.execute_script("window.scrollBy(0, 300);")
        nested_list = [el.text.split('\n') for el in elements]
        return nested_list[0]

    def drag_like_a_human(self, driver, source, target):
        ActionChains(driver) \
            .click_and_hold(source) \
            .move_to_element(target) \
            .pause(0.5) \
            .release() \
            .perform()