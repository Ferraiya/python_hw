from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from config import BASE_URL, BASE_BROWSER


class Browser:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, browser_name=BASE_BROWSER, headless=False):
        if hasattr(self, 'driver'):
            return

        self.browser_name = browser_name
        self.headless = headless

        options = Options()
        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless")

        if browser_name == 'chrome':
            self.driver = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            self.driver = webdriver.Firefox()

        self.actions = ActionChains(self.driver)

    def go_to_main_page(self):
        if self.driver.current_url != BASE_URL:
            self.driver.get(BASE_URL)