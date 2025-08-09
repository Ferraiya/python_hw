from src.pages.elements_pages.sortable_page import SortablePage
from time import sleep

class TestDragAndDrop:

    def test_drag_and_drop_of_line_items(self, driver):
        sortable_page = SortablePage(driver)
        sortable_page.open()

        before = sortable_page.content_of_items(driver)

        assert before == ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
        sor = sortable_page.get_element(sortable_page.source)
        targ = sortable_page.get_element(sortable_page.target)
        sleep(3)
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "locator")))
        sor.click()
        sortable_page.drag_like_a_human(driver, sor, targ)
        sleep(1)
        after = sortable_page.content_of_items(driver)
        assert after == ['One', 'Five', 'Two', 'Three', 'Four', 'Six']

    def test_drag_and_drop_of_grid_items(self, driver):
        sortable_page = SortablePage(driver)
        sortable_page.open()
        sortable_page.grid_click()
        sleep(1)
        before = sortable_page.content_of_grid_items(driver)

        assert before == ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

        sor = sortable_page.get_element(sortable_page.source_grid)
        targ = sortable_page.get_element(sortable_page.target_grid)
        sleep(1)
        sor.click()
        sortable_page.drag_like_a_human(driver, sor, targ)
        sleep(1)
        after = sortable_page.content_of_grid_items(driver)
        sleep(2)
        assert after == ['One', 'Two', 'Three', 'Four', 'Six', 'Seven', 'Eight', 'Nine', 'Five']