from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from config import BASE_URL, BASE_TIMEOUT, BASE_BROWSER


class Browser:
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = None

    def __init__(cls, browser_name=BASE_BROWSER, headless=False):
        cls.browser_name = browser_name
        cls.headless = headless
        if headless:
            cls.options.add_argument("--headless")
        if cls.browser_name == 'chrome':
            cls.driver = webdriver.Chrome(options=cls.options)
        elif cls.browser_name == 'firefox':
            cls.driver = webdriver.Firefox(options=cls.options)
        if cls.driver:
            cls.actions = ActionChains(cls.driver)

    def go_to_main_page(self):
        if self.driver.current_url != BASE_URL:
            self.driver.get(BASE_URL)

    def get_element(self, locator, by_=By.XPATH):
        return self.driver.find_element(by_, locator)

    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        self.actions.scroll_to_element(element)

    def wait_for_clickable(self, locator, by_ =By.XPATH, timeout=BASE_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable((by_, locator)))

    def click(self, locator):
        element = self.get_element(locator)
        self.scroll_to_element(locator)
        self.wait_for_clickable(locator)
        element.click()




