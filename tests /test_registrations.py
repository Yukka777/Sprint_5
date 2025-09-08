from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data
import random


class TestRegistrations:
    def test_registrations_success(self, get_empty_driver):
        driver = get_empty_driver
        driver.get(data.URLS.MAIN)
        driver.find_element(*Locators.BUTTON_ENTER_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TEXT_ENTER))
        driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TITLE_REGISTRATION))

        elements = driver.find_elements(*Locators.NAME_EMAIL_FIELD)
        elements[0].send_keys(data.Auth.name)
        elements[1].send_keys('ruslan_khalitov_6_' + str(random.randint(100, 1000)) + '@domen.ru')

        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        password_field.send_keys('12345')

        button_registrate = driver.find_element(*Locators.BUTTON_REGISTRATION)
        button_registrate.click()

        assert driver.find_element(*Locators.INCORRECT_PASSWORD_TEXT)

        password_field.send_keys('123456')
        button_registrate.click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TEXT_ENTER))
        assert driver.find_element(*Locators.TEXT_ENTER)
