from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from data import  TestLinks, TestUser
from locators import Locators

class TestLogin:

    #вход по кнопке «Войти в аккаунт» на главной,
    def test_login_by_button_login_to_account(self, driver, login):
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_MAKE_ORDER))
        assert driver.current_url == TestLinks.main_url+"/"

    def make_login(self, driver):
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_USER_EMAIL)).send_keys(TestUser.email)
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_USER_PASSWORD)).send_keys(TestUser.password)
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGIN)).click()
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_MAKE_ORDER))
        assert driver.current_url == TestLinks.main_url + "/"

    #вход через кнопку «Личный кабинет»,
    def test_login_by_user_account_link(self, driver):
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()
        self.make_login(driver)

    #вход через кнопку в форме регистрации,
    def test_login_from_form_recover_password(self, driver):
        driver.get(TestLinks.main_url+"/register")
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_LOGIN)).click()
        self.make_login(driver)


    # вход через кнопку в форме восстановления пароля.
    def test_login_from_form_user_registration(self, driver):
        driver.get(TestLinks.main_url + "/forgot-password")
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.LINK_LOGIN)).click()
        self.make_login(driver)
