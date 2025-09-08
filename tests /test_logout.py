from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogout:
    def test_logout_success(self, get_logged_driver):
        driver = get_logged_driver
        driver.find_element(*Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TEXT_FROM_PROFILE))
        driver.find_element(*Locators.BUTTON_EXIT).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.TEXT_ENTER))
        assert driver.find_element(*Locators.TEXT_ENTER)
