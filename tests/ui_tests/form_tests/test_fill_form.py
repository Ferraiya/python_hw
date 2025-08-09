from src.pages.forms_pages.form_page import FormPage
from faker import Faker
import random
from time import sleep


class TestForm:

    color_invalid = ["rgb(220, 53, 69)", "#dc3545"]
    symbol_invalid = "stroke"
    color_valid = ["rgb(40, 167, 69)", "#28a745"]
    symbol_valid = "fill"

    def test_fill_form_positive(self, driver):
        fake = Faker()
        form = FormPage(driver)
        phone = str(random.randint(0000000000, 9999999999))
        year = "2000"
        month = "1"
        month_name = "February"
        day = "18"
        female = 2
        full_date = f"{day} Feb {year}"
        search_state = "NC"
        search_city = "da"
        state = "NCR"
        city = "Noida"

        form.open()

        form.wait_for(form.email_selector)
        form.set_firstname(fake.first_name())
        form.set_lastname(fake.last_name())
        form.set_email(fake.email())
        form.set_gender(female)
        form.set_mobile(phone)
        form.set_date_of_birth(month, month_name, year, day, full_date)
        form.set_subject(driver)
        form.set_hobby()
        form.upload_picture()
        form.set_address(fake.address())
        form.select_state(search_state, state)
        form.select_city(search_city, city)

        form.submit()
        form.assert_success_message()

    def test_empty_form_negative(self, driver):
        form = FormPage(driver)

        form.open()
        form.wait_for(form.email_selector)
        form.scroll_down(driver)
        form.wait_for_clickable(form.submit_button_selector)
        form.submit()
        form.wait_for_valid_style(form.date_of_birth_selector)

        form.assert_field_is_validated(driver, form.firstname_selector, self.color_invalid, self.symbol_invalid)
        form.assert_field_is_validated(driver, form.lastname_selector, self.color_invalid, self.symbol_invalid)
        form.assert_field_is_validated(driver, form.mobile_selector, self.color_invalid, self.symbol_invalid)

    def test_fill_form_negative(self, driver):
        fake = Faker()
        form = FormPage(driver)
        phone = str(random.randint(000, 999))
        other = 3
        email = "qwerty"

        form.open()
        form.wait_for(form.email_selector)

        form.set_firstname(fake.first_name())
        form.set_lastname(fake.last_name())
        form.set_email(email)
        form.set_gender(other)
        form.set_mobile(phone)

        form.scroll_down(driver)
        form.wait_for_clickable(form.submit_button_selector)
        form.submit()
        form.wait_for_valid_style(form.date_of_birth_selector)

        form.assert_field_is_validated(driver, form.email_selector, self.color_invalid, self.symbol_invalid)
        form.assert_field_is_validated(driver, form.mobile_selector, self.color_invalid, self.symbol_invalid)

        form.assert_field_is_validated(driver, form.firstname_selector, self.color_valid, self.symbol_valid)
        form.assert_field_is_validated(driver, form.lastname_selector, self.color_valid, self.symbol_valid)
        form.assert_field_is_validated(driver, form.address_selector, self.color_valid, self.symbol_valid)