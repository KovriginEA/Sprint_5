from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from data import  TestLinks
from locators import Locators

class TestNavigationToUserAccount:
    def test_navigation_to_user_account_after_login(self, driver, login):
        # Клик по кнопке «Личный кабинет»
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        WDW(driver, 5).until(EC.visibility_of_element_located(Locators.TEXT_PROFILE))
        assert driver.find_element(*Locators.TEXT_PROFILE).is_displayed()