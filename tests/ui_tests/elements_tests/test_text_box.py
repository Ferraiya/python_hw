class TestTextBox:

    def test_fill_in_form_valid_data(self,text_box_page):
        text_box_page.open()
        text_box_page.full_name_input.set_value("First name")
        text_box_page.browser.click(text_box_page.submit_button)