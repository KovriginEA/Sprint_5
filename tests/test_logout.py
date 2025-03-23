from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from data import  TestLinks
from locators import Locators

class TestLogout:

    def test_logout_from_account(self, driver, login):
        #Клик по кнопке «Личный кабинет»
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        #Клик по кнопке «Выход»
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGOUT)).click()
        #Проверка перехода на страницу логина
        WDW(driver, 8).until(EC.url_to_be(TestLinks.main_url+"/login"))
        assert driver.find_element(*Locators.BUTTON_LOGIN).is_displayed()