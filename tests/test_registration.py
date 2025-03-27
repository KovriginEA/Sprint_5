from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from data import  TestLinks, TestUser
from locators import Locators
from support import *

class TestRegistration:
    # Успешную регистрацию.
    def test_succes_registration(self, driver):
        driver.get(TestLinks.main_url+"/register")
        random_email = generate_email()
        random_password = generate_password(6)

        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.REG_NAME)).send_keys(TestUser.name)
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.REG_EMAIL)).send_keys(random_email)
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.REG_PASSWORD)).send_keys(random_password)
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_REG_SUBMIT)).click()
        WDW(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_LOGIN))

        assert  driver.find_element(*Locators.BUTTON_LOGIN).is_displayed()


    #Ошибку для некорректного пароля.
    def test_error_message_for_wrong_password(self, driver):
        driver.get(TestLinks.main_url + "/register")
        random_email = generate_email()
        random_password = generate_password(4)

        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.REG_NAME)).send_keys(TestUser.name)
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.REG_EMAIL)).send_keys(random_email)
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.REG_PASSWORD)).send_keys(random_password)
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_REG_SUBMIT)).click()
        WDW(driver, 5).until(EC.visibility_of_element_located(Locators.TEXT_WRONG_PASSWORD))

        assert driver.find_element(*Locators.TEXT_WRONG_PASSWORD).is_displayed()
