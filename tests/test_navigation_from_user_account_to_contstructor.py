from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from data import  TestLinks
from locators import Locators

class TestNavigationFromUserAccountToConstructor:

    def test_click_on_constructor_follow_to_constructor(self, driver, login):
        #клик по кнопке «Личный кабинет»
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        WDW(driver, 5).until(EC.visibility_of_element_located(Locators.TEXT_PROFILE))

        #клик по надписи конструктор
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_CONSTRUCTOR)).click()
        WDW(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_MAKE_ORDER))

        assert driver.current_url == TestLinks.main_url+"/"


    def test_click_on_logo_follow_to_constructor(self, driver, login):
        #клик по кнопке «Личный кабинет»
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        WDW(driver, 5).until(EC.visibility_of_element_located(Locators.TEXT_PROFILE))

        # клик по логотипу
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO_STELLAR)).click()
        WDW(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_MAKE_ORDER))

        assert driver.current_url == TestLinks.main_url+"/"