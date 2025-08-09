import random
import pytest
import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

class CalendarElement:
    month = "5"
    year = "2000"
    day = "28"
    firstname_xpath = '//input[@id="firstName"]'
    lastname_xpath = '//input[@id="lastName"]'
    email_xpath = '//input[@id="userEmail"]'
    gender_radio_xpath = '//label[@for="gender-radio-1"]'
    mobile_xpath = '//input[@id="userNumber"]'
    date_of_birth_xpath = '//input[@id="dateOfBirthInput"]'
    year_xpath = '//input[@class="react-datepicker__year-select"]'
    year_option_xpath = f'//option[@value="{year}"]'
    month_option_xpath = f'//option[@value="{month}"]'
    month_xpath = '//input[@class="react-datepicker__month-select"]'
    hobby = '//label[@for="hobbies-checkbox-3"]'
    subject_field = '//input[@id="subjectsContainer"]'
    subject_dropdown = '//div[@class="subjects-auto-complete__menu"]'
    upload_xpath = '//input[@id="uploadPicture"]'
    address_xpath = '//textarea[@id="currentAddress"]'
    state_xpath = '//div[contains(@class,"-indicatorContainer")]'


    firstname = driver.find_element(By.XPATH, firstname_xpath)
    lastname = driver.find_element(By.XPATH, lastname_xpath)
    email = driver.find_element(By.XPATH, email_xpath)
    gender = driver.find_element(By.XPATH, gender_radio_xpath)
    mobile = driver.find_element(By.XPATH, mobile_xpath)
    date_field = driver.find_element(By.XPATH, date_of_birth_xpath)
    year = driver.find_element(By.XPATH, year_xpath)
    hobby = driver.find_element(By.XPATH, hobby)
    address = driver.find_element(By.XPATH, address_xpath)
    submit_button = driver.find_element(By.ID, "submit")

    def scroll_down(self, place):
        driver.execute_script("arguments[0].scrollIntoView(true);", place)

class CalendarElement:
    month_picker = '//*[contains(@class, "month-select")]'
    current_month = '//[contains(@class, "current-month")]'
    year_picker = '//*[contains(@class, "year-select")]'
    month_locator = '//option[text()="%s"]'
    date_of_birth_input = '//*[@id="dateOfBirthInput"]'

        def __init__(self, locator, driver):
            self.locator = locator
            self.driver = driver

        def month_select(self, month):
            wait.until(EC.element_to_be_clickable(By.XPATH, self.month_picker))
            self.driver.find_element(By.XPATH, self.month_picker).click()
            wait.until(EC.element_to_be_clickable(By.XPATH, self.month_locator % month))
            self.driver.find_element(By.XPATH, self.month_locator % month).click()
            wait.until(EC.text_to_be_present_in_element(By.XPATH, self.current_month), month)

            actual_value = self.driver.find_element(By.XPATH, self.date_of_birth_input).get_attribute("value")

class FieldElement:
    def set_value(self, value):
        wait.until(EC.element_to_be_clickable(By.XPATH, self.month_picker))
        self.driver.find_element(By.XPATH, self.month_picker).send_keys(value)

class SelectElement:
    def set_value(self, value):
        wait.until(EC.element_to_be_clickable(By.XPATH, self.month_picker))
        self.driver.find_element(By.XPATH, self.month_picker).click()
        wait.until(EC.element_to_be_clickable(By.XPATH, self.month_picker))

class PracticeForm():
    def __init__(self):
        self.date_of_birth_calendar = CalendarElement('//*[@id="dateOfBirthInput]')
        self.first_name = FieldElement('firstname')

    self.date_of_birth_calendar.month_select()


# test

def test_login():
    practice_form = PracticeForm()
    practice_form.first_name.set_value()
