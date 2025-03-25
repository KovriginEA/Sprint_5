from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from data import  TestLinks, TestUser
from locators import Locators


def make_login(driver):
    WDW(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_USER_EMAIL)).send_keys(TestUser.email)
    WDW(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_USER_PASSWORD)).send_keys(TestUser.password)
    WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGIN)).click()
    WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_MAKE_ORDER))
