from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructor:

    def test_jump_to_buns_success(self, get_logged_driver):
        driver = get_logged_driver
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUILD_BURGER_TEXT))

        button_buns = driver.find_element(*Locators.BUTTON_BUNS)
        button_sauces = driver.find_element(*Locators.BUTTON_SAUCES)
        button_sauces.click()
        button_buns.click()
        assert 'current' in button_buns.find_element(*Locators.ELEMENTS_PARENT).get_attribute('class')

    def test_jump_to_sauces_success(self, get_logged_driver):
        driver = get_logged_driver
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUILD_BURGER_TEXT))
        button_sauces = driver.find_element(*Locators.BUTTON_SAUCES)
        button_sauces.click()
        assert 'current' in button_sauces.find_element(*Locators.ELEMENTS_PARENT).get_attribute('class')

    def test_jump_to_fillings_success(self, get_logged_driver):
        driver = get_logged_driver
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.BUILD_BURGER_TEXT))
        button_fillings = driver.find_element(*Locators.BUTTON_FILLINGS)
        button_fillings.click()
        assert 'current' in button_fillings.find_element(*Locators.ELEMENTS_PARENT).get_attribute('class')
