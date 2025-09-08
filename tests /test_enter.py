from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data


class TestEnter:
    def test_enter_from_main_success(self, get_empty_driver):
        driver = get_empty_driver
        driver.get(data.URLS.MAIN)
        driver.find_element(*Locators.BUTTON_ENTER_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TEXT_ENTER))

        driver.find_element(*Locators.NAME_EMAIL_FIELD).send_keys(data.Auth.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(data.Auth.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUTTON_PLACE_ORDER))
        assert driver.find_element(*Locators.BUTTON_PLACE_ORDER)

    def test_enter_from_personal_area_success(self, get_empty_driver):
        driver = get_empty_driver
        driver.get(data.URLS.LOGIN)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TEXT_ENTER))
        driver.find_element(*Locators.NAME_EMAIL_FIELD).send_keys(data.Auth.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(data.Auth.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUTTON_PLACE_ORDER))
        assert driver.find_element(*Locators.BUTTON_PLACE_ORDER)

    def test_enter_from_registration_success(self, get_empty_driver):
        driver = get_empty_driver
        driver.get(data.URLS.REG)
        driver.find_element(*Locators.ENTER_LINK).click()
        driver.find_element(*Locators.NAME_EMAIL_FIELD).send_keys(data.Auth.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(data.Auth.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUTTON_PLACE_ORDER))
        assert driver.find_element(*Locators.BUTTON_PLACE_ORDER)

    def test_enter_from_password_recovery_success(self, get_empty_driver):
        driver = get_empty_driver
        driver.get(data.URLS.FORGOT_PASS)
        driver.find_element(*Locators.ENTER_LINK).click()
        driver.find_element(*Locators.NAME_EMAIL_FIELD).send_keys(data.Auth.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(data.Auth.password)
        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUTTON_PLACE_ORDER))
        assert driver.find_element(*Locators.BUTTON_PLACE_ORDER)
