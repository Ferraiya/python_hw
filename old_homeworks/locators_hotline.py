import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, timeout=10)

@pytest.fixture
def open_url():
    driver.get("https://hotline.ua")

def test_elements_menu_present(open_url):

    driver.find_element(By.XPATH, '//*[normalize-space(@class)="button-menu-main"]').click()
    driver.find_element(By.XPATH, '//a[contains(@href,"/hotline.finance/")]')
    driver.find_element(By.XPATH, '//*[@data-id="898"]')
    driver.find_element(By.XPATH, '//*[@class="menu-main__sub-sections"]//a[@href="/ua/auto/avtomobilnye-masla/"]')

def test_categories_main_menu_present(open_url):
    driver.find_element(By.XPATH, '//*[@data-eventlabel="LEGO"]')
    driver.find_element(By.XPATH, '//*[@class="tabs-list__item" and contains(text(),"Телевізори")]')

def test_search_field_present(open_url):
    driver.find_element(By.ID, 'mainSearchBlock')
    driver.find_element(By.XPATH, '//*[@id="mainSearchBlock"]//input')

def test_login_icon_present(open_url):
    driver.find_element(By.CSS_SELECTOR, 'a.login-button svg')

def test_fill_login_form():
    driver.find_element(By.CSS_SELECTOR, 'a.login-button').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    email_field.send_keys("test@test.ua")
    password_field = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    password_field.send_keys("12345asdffdge")


