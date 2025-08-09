import pytest
from src.pages.elements_pages.checkbox_page import CheckboxPage
from time import sleep

@pytest.mark.parametrize("label, checked_labels, half_checked_labels", [
    ("veu", "check", ["documents", "workspace", "home"])
])
def test_check_single_checkbox_and_verify_parents(driver, label, checked_labels, half_checked_labels):
    checkbox_page = CheckboxPage(driver)
    checkbox_page.open()
    checkbox_page.scroll_down(driver)
    checkbox_page.expand_all()

    box = checkbox_page.checkbox(label)
    checkbox_page.click(box)
    checkbox_page.assert_checkbox_state("veu", "check")



    # # Проверка родительских half-checked состояний, если есть
    # for loc in half_checked_locators:
    #     assert checkbox_page.el_count(getattr(checkbox_page, loc)) == 1
    #
    # # Деактивировать чекбокс
    # checkbox_page.click(getattr(checkbox_page, checkbox_locator))
    #
    # # Проверки, что всё снялось
    # assert checkbox_page.el_count(getattr(checkbox_page, checked_locator)) == 0
    # for loc in half_checked_locators:
    #     assert checkbox_page.el_count(getattr(checkbox_page, loc)) == 0

# from src.pages.elements_pages.checkbox_page import CheckboxPage
#
#
# class TestCheckBoxes:
#
#     def test_check_home_box(self, driver):
#         checkbox_page = CheckboxPage(driver)
#         checkbox_page.open()
#         checkbox_page.scroll_down(driver)
#         checkbox_page.click_all(checkbox_page.button_collapsed)
#
#         sleep(15)
#
#         checkbox_page.click(checkbox_page.home_box)
#         assert checkbox_page.el_count(checkbox_page.text_success) == 17
#         checkbox_page.assert_success_text_color()
#
#         box = checkbox_page.get_element(checkbox_page.checkbox)
#         checkbox_page.assert_checked_icon(box)
#
#         checkbox_page.click(checkbox_page.toggle_button)
#         checkbox_page.click_all(checkbox_page.button_collapsed)
#
#         boxes = checkbox_page.get_elements(checkbox_page.checkbox)
#         for box in boxes:
#             checkbox_page.assert_checked_icon(box)
#
#         sleep(15)
#         checkbox_page.click(checkbox_page.home_box)
#         assert checkbox_page.el_count(checkbox_page.text_success) == 0
#
#     def test_check_children_are_unchecked_if_collapsed(self, driver):
#         checkbox_page = CheckboxPage(driver)
#         checkbox_page.open()
#         checkbox_page.scroll_down(driver)
#
#         assert checkbox_page.el_count(checkbox_page.icon_closed) == 1
#         assert checkbox_page.el_count(checkbox_page.icon_open) == 0
#
#         # Expand first level
#         checkbox_page.click(checkbox_page.toggle_button)
#         assert checkbox_page.el_count(checkbox_page.button_expanded) == 1
#         assert checkbox_page.el_count(checkbox_page.button_collapsed) == 3
#         assert checkbox_page.el_count(checkbox_page.icon_closed) == 3
#         assert checkbox_page.el_count(checkbox_page.icon_open) == 1
#
#     def test_check_parents_are_halfchecked_if_child_checked(self, driver):
#         checkbox_page = CheckboxPage(driver)
#         checkbox_page.open()
#         checkbox_page.scroll_down(driver)
#
#         # Expand all levels
#         checkbox_page.click_all(checkbox_page.button_collapsed)
#         assert checkbox_page.el_count(checkbox_page.button_expanded) == 4
#         assert checkbox_page.el_count(checkbox_page.button_collapsed) == 2
#
#         assert checkbox_page.el_count(checkbox_page.icon_closed) == 2
#         assert checkbox_page.el_count(checkbox_page.icon_open) == 4
#
#         # Collapse all levels
#         checkbox_page.click_all(checkbox_page.button_collapsed)
#         assert checkbox_page.el_count(checkbox_page.button_expanded) == 6
#
#         assert checkbox_page.el_count(checkbox_page.icon_closed) == 0
#         assert checkbox_page.el_count(checkbox_page.icon_open) == 6
#
#         # Expand second level
#         checkbox_page.click(checkbox_page.documents_toggle)
#         assert checkbox_page.el_count(checkbox_page.icon_closed) == 1
#         assert checkbox_page.el_count(checkbox_page.icon_open) == 3
#
#     def test_check_child_half_check_parent(self, driver):
#         checkbox_page = CheckboxPage(driver)
#         checkbox_page.open()
#
#         checkbox_page.click(checkbox_page.toggle_button)
#         checkbox_page.click(checkbox_page.documents_toggle)
#         checkbox_page.click(checkbox_page.workspace_toggle)
#         checkbox_page.click(checkbox_page.veu_checkbox)
#
#         assert checkbox_page.veu_checked
#         assert checkbox_page.documents_half_checked
#         assert checkbox_page.workspace_half_checked
#
#     def test_if_parent_collapsed_children_are_checked(self, driver):
#         checkbox_page = CheckboxPage(driver)
#         checkbox_page.open()
#
#         checkbox_page.click(checkbox_page.toggle_button)
#         checkbox_page.click(checkbox_page.documents_toggle)
#         checkbox_page.click(checkbox_page.documents_checkbox)
#         checkbox_page.click(checkbox_page.workspace_toggle)
#         checkbox_page.click(checkbox_page.office_toggle)
#
#         assert checkbox_page.documents_checked
#         assert checkbox_page.children_boxes_checked
#
#
#
