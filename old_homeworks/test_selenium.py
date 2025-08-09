from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=1920,1080")
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, timeout=10)

def test_smth():
    driver.get('https://hotline.ua')
    # power_systems_buttons = driver.find_element(By.XPATH, '//div[@class="categories-section__inner"]//a[@href="/ua/power/"]')
    # power_systems_buttons.click()
    driver.find_element(By.XPATH, '//*[normalize-space(@class)="button-menu-main"]').click()
    # driver.implicitly_wait(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="menu-main__item"]/a[@href="/ua/auto/"]')))
    driver.find_element(By.XPATH, '//*[@class="menu-main__item"]/a[@href="/ua/auto/"]').click()
