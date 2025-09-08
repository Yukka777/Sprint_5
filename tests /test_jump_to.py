from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestJumpTo:
    def test_jump_to_personal_area_success(self, get_logged_driver):
        driver = get_logged_driver
        driver.find_element(*Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TEXT_FROM_PROFILE))
        assert driver.find_element(*Locators.TEXT_FROM_PROFILE)

    def test_jump_to_constructor_success(self, get_logged_driver):
        driver = get_logged_driver
        driver.find_element(*Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TEXT_FROM_PROFILE))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(*Locators.BUILD_BURGER_TEXT)

    def test_jump_to_constructor_by_main_logo_success(self, get_logged_driver):
        driver = get_logged_driver
        driver.find_element(*Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TEXT_FROM_PROFILE))

        driver.find_element(*Locators.BUTTON_MAIN_LOGO).click()
        assert driver.find_element(*Locators.BUILD_BURGER_TEXT)
