from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from data import  TestLinks
from locators import Locators
from support import make_login

class TestLogin:

    #вход по кнопке «Войти в аккаунт» на главной,
    def test_login_by_button_login_to_account(self, driver, login):
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_MAKE_ORDER))
        assert driver.current_url == TestLinks.main_url+"/"



    #вход через кнопку «Личный кабинет»,
    def test_login_by_user_account_link(self, driver):
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        make_login(driver)
        assert driver.current_url == TestLinks.main_url + "/"

    #вход через кнопку в форме регистрации,
    def test_login_from_form_recover_password(self, driver):
        driver.get(TestLinks.main_url+"/register")
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_LOGIN)).click()
        make_login(driver)
        assert driver.current_url == TestLinks.main_url + "/"


    # вход через кнопку в форме восстановления пароля.
    def test_login_from_form_user_registration(self, driver):
        driver.get(TestLinks.main_url + "/forgot-password")
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_LOGIN)).click()
        make_login(driver)
        assert driver.current_url == TestLinks.main_url + "/"
