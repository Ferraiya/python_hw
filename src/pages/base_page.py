from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from config import BASE_TIMEOUT

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for(self, el):
        return self.wait.until(EC.visibility_of_element_located(el))

    def wait_disappear(self, el):
        return self.wait.until(EC.invisibility_of_element(el))

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def scroll_to_element(self, locator):
        element = self.wait_for(locator)
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).perform()

    def scroll_down(self, driver):
        driver.execute_script("window.scrollBy(0, 250);")

    def scroll_up(self, driver):
        driver.execute_script("window.scrollBy(0, 0);")

    def wait_for_clickable(self, locator, timeout=BASE_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.scroll_to_element(locator)
        element = self.wait_for_clickable(locator)
        element.click()

    def click_all(self, el):
        elements = self.driver.find_elements(*el)
        for element in elements:
            self.scroll_to_element(el)
            self.wait_for_clickable(el)
            element.click()

    def assert_el_disappears(self, driver, el):
        assert not driver.find_elements(el)

    def close_vigniete(self):
        self.get_element((By.ID, "dismiss-button")).click()

    def el_count(self, el):
        return len(self.get_elements(el))

    def wait_for_valid_style(self, locator, expected_color_part="40", timeout=5):
        WebDriverWait(self.driver, timeout).until(
            lambda d: expected_color_part in d.find_element(*locator).value_of_css_property("border-color")
        )

