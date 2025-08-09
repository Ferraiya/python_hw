from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.pages.base_page import BasePage
from config import BASE_URL
import os


class FormPage(BasePage):

    page_url = BASE_URL + "/automation-practice-form"
    full_name_input = (By.XPATH, '//*[@id="userName"]')
    submit_button_selector = (By.XPATH, '//*[@id="submit"]')
    result_selector = (By.XPATH, '//svg[contains(@class,"fa-check-circle")]')
    firstname_selector = (By.XPATH, '//*[@id="firstName"]')
    lastname_selector = (By.XPATH, '//*[@id="lastName"]')
    email_selector = (By.XPATH, '//*[@id="userEmail"]')
    mobile_selector = (By.XPATH, '//*[@id="userNumber"]')
    date_of_birth_selector = (By.XPATH, '//*[@id="dateOfBirthInput"]')
    year_selector = (By.XPATH, '//select[@class="react-datepicker__year-select"]')
    month_selector = (By.CLASS_NAME, "react-datepicker__month-select")
    current_month_selector = (By.XPATH, '//select[@class="react-datepicker__current-month"]')
    hobby_selector = (By.XPATH, '//label[@for="hobbies-checkbox-3"]')
    subject_selector = (By.XPATH, '//*[@id="subjectsContainer"]')
    subject_dropdown_selector = (By.XPATH, '//div[@class="subjects-auto-complete__control--menu-is-open"]')
    subject_input_selector = (By.XPATH, '//*[@id="subjectsInput"]')
    subject_chosen_selector = (By.CLASS_NAME, 'subjects-auto-complete__multi-value__label')
    subject_selected = (By.XPATH, '//*[contains(text(), "Maths")]')
    upload_selector = (By.XPATH, '//*[@id="uploadPicture"]')
    address_selector = (By.XPATH, '//*[@id="currentAddress"]')
    state_selector = (By.XPATH, '//*[@id="react-select-3-input"]')
    city_selector = (By.XPATH, '//*[@id="react-select-4-input"]')
    thanks_message_selector = (By.XPATH, '//*[@id="example-modal-sizes-title-lg"]')
    close_modal_selector =(By.XPATH, '//*[@id="closeLargeModal"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.page_url)

    def month_option_select(self, month):
        return (By.XPATH, f'//option[@value="{month}"]')

    def year_option_select(self, year):
        return (By.XPATH, f'//option[@value="{year}"]')

    def day_option_select(self, day):
        return (
            By.XPATH,
            f'//div[contains(@class, "react-datepicker__day") '
            f'and not(contains(@class, "react-datepicker__day--outside-month")) '
            f'and text()="{day}"]'
        )

    def state_menu_item_selector(self, state):
        return (By.XPATH, f'//*[contains(text(), "{state}")]')

    def city_menu_item_selector(self, city):
        return (By.XPATH, f'//*[contains(text(), "{city}")]')

    def set_firstname(self, value):
        self.wait_for(self.firstname_selector)
        self.get_element(self.firstname_selector).send_keys(value)

    def set_lastname(self, value):
        self.wait_for(self.lastname_selector)
        self.get_element(self.lastname_selector).send_keys(value)

    def set_email(self, value):
        self.wait_for(self.email_selector)
        self.get_element(self.email_selector).send_keys(value)

    def set_gender(self, value):
        gender_radio_selector = (By.XPATH, f'//label[@for="gender-radio-{value}"]')
        self.get_element(gender_radio_selector).click()

    def set_mobile(self, value):
        self.get_element(self.mobile_selector).send_keys(value)

    def set_month(self, month, month_name):
        self.get_element(self.date_of_birth_selector).click()
        self.wait_for(self.month_selector)
        self.get_element(self.month_selector).click()

        month_option_locator = self.month_option_select(month)
        self.wait_for(month_option_locator)
        self.get_element(month_option_locator).click()

    def set_year(self, year):
        self.wait_for(self.year_selector)
        self.get_element(self.year_selector).click()
        year_option_locator = self.year_option_select(year)
        self.wait_for(year_option_locator)
        self.get_element(year_option_locator).click()
        self.get_element(self.year_selector).click()

    def set_day(self, day, full_date):
        day_locator = self.day_option_select(day)
        self.wait_for(day_locator)
        self.get_element(day_locator).click()
        self.wait_for(self.date_of_birth_selector)
        assert self.get_element(self.date_of_birth_selector).get_attribute("value") == full_date

    def set_date_of_birth(self, month, month_name, year, day, full_date):
        self.get_element(self.date_of_birth_selector).click()
        self.set_month(month, month_name)
        self.set_year(year)
        self.set_day(day, full_date)

    def set_subject(self, driver):
        self.scroll_down(driver)
        self.wait_for(self.subject_input_selector)
        subject_input = self.get_element(self.subject_input_selector)
        subject_input.click()
        subject_input.send_keys("Mat")

        self.wait_for_clickable(self.subject_selected)
        self.get_element(self.subject_selected).click()

    def scroll_down(self, driver):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_element(self.address_selector))

    def set_hobby(self):
        self.wait_for_clickable(self.hobby_selector)
        self.get_element(self.hobby_selector).click()

    def upload_picture(self):
        self.wait_for_clickable(self.upload_selector)
        upload_file = os.path.abspath("homework1-example-Ferraiya/src/Data/Logo.png")
        self.get_element(self.upload_selector).send_keys(upload_file)

    def set_address(self, value):
        self.wait_for_clickable(self.address_selector)
        self.get_element(self.address_selector).send_keys(value)

    def select_state(self, value, state):
        self.wait_for_clickable(self.state_selector)
        self.get_element(self.state_selector).send_keys(value)
        state_locator = self.state_menu_item_selector(state)
        self.wait_for(state_locator)
        self.get_element(state_locator).click()

    def select_city(self, value, city):
        self.wait.until(EC.element_to_be_clickable(self.city_selector))
        self.get_element(self.city_selector).send_keys(value)
        city_locator = self.city_menu_item_selector(city)
        self.wait_for(city_locator)
        self.get_element(city_locator).click()

    def submit(self):
        self.wait_for_clickable(self.submit_button_selector)
        self.get_element(self.submit_button_selector).click()

    def assert_success_message(self):
        self.wait_for(self.thanks_message_selector)
        assert self.get_element(self.thanks_message_selector).is_displayed()

    def close_success_modal(self):
        self.wait_for_clickable(self.close_modal_selector)
        self.get_element(self.close_modal_selector).click()

    def assert_field_is_validated(self, driver, selector, color, symbol):
        element = driver.find_element(*selector)
        border_color = element.value_of_css_property("border-color")
        assert border_color in color
        bg_image = element.value_of_css_property("background-image")
        assert symbol in bg_image

