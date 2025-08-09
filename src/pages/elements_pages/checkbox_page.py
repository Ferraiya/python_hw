from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import BASE_URL

class CheckboxPage(BasePage):
    page_url = BASE_URL + "/checkbox"
    home_box = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]')
    toggle_button = (By.XPATH, '//*[@title ="Toggle"]')
    icon_closed =  (By.XPATH, '//*[@class="rct-icon-parent-close"]')
    icon_open = (By.XPATH, '//*[@class="rct-icon-parent-open"]')
    result = (By.XPATH, '//*[@id = "result"]')
    text_success = (By.XPATH, '//*[@class ="text-success"]')


    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.page_url)

    def assert_success_text_color(self):
        element = self.get_element(self.text_success)
        color = element.value_of_css_property("color")
        assert color == "rgba(40, 167, 69, 1)"

    def icon_state(self, state):
        icon_state = (By.XPATH, f'//*[@class="rct-icon rct-icon-expand-{state}"]')
        return icon_state

    def checkbox(self, item):
        checkbox = (By.XPATH, f'//label[@for="tree-node-{item}"]/span[@class="rct-checkbox"]')
        return checkbox

    def checkbox_state(self, item, icon_class_part):
        return (By.XPATH,
                f'//label[@for="tree-node-{item}"]/span[@class="rct-checkbox"]/*[contains(@class, "rct-icon-{icon_class_part}")]')

    def assert_checkbox_state(self, el, expected_state):
        element = self.checkbox_state(el, expected_state)
        assert self.el_count(element)>0

    def expand_all(self):
        collapsed = self.icon_state("close")
        self.wait_for_clickable(collapsed)
        assert self.get_element(collapsed).is_displayed()
        while self.el_count(collapsed) > 0:
            self.click_all(collapsed)

    def icon_svg(self, text):
        icon_xpath = (By.XPATH, f'//*[text()="{text}"]//span[@class="rct-icon rct-node-icon"]/svg')
        return icon_xpath

    def is_checked(self, checkbox_text):
        checked_xpath = f"//*[text()='{checkbox_text}']/span[contains(@class, 'rct-icon-check')]"
        return len(self.driver.find_elements(By.XPATH, checked_xpath)) > 0

    def is_half_checked(self, checkbox_text):
        checked_xpath = f"//*[text()='{checkbox_text}']/span[contains(@class, 'rct-icon-half-check')]"
        return len(self.driver.find_elements(By.XPATH, checked_xpath)) > 0

    def section_toggle(self, section_text):
        toggle_xpath = self.driver.find_element(By.XPATH, f"//label[span[text()='{section_text}']]/preceding-sibling::button")
        return toggle_xpath


    # def get_checkbox_state(self, label_text):
    #     checkbox_icon = self.driver.find_element(
    #         By.XPATH, f"//*[text()='{label_text}']/following-sibling::span[contains(@class, 'rct-icon')]"
    #     )
    #     icon_class = checkbox_icon.get_attribute("class")
    #     if "rct-icon-check" in icon_class:
    #         return "checked"
    #     elif "rct-icon-half-check" in icon_class:
    #         return "half-checked"
    #     else:
    #         return "unchecked"