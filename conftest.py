import pytest
from selenium import webdriver
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data

@pytest.fixture(scope='function')
def get_empty_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--windows-size=1920,1080')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()

    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def get_logged_driver(get_empty_driver):
    driver = get_empty_driver
    driver.get(data.URLS.MAIN)
    driver.find_element(*Locators.BUTTON_ENTER_TO_ACCOUNT).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TEXT_ENTER))
    driver.find_element(*Locators.NAME_EMAIL_FIELD).send_keys(data.Auth.email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(data.Auth.password)
    driver.find_element(*Locators.BUTTON_ENTER).click()

    yield driver
    driver.quit()
