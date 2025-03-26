from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from data import  TestLinks, TestUser
from locators import Locators
from support import *
import time

class TestRegistration:
    # Успешную регистрацию.
    # Поле «Имя» должно быть не пустым;
    # в поле Email введён email в формате логин@домен: например, 123@ya.ru.
    # Минимальный пароль — шесть символов.
    def test_succes_registration(self, driver):
        driver.get(TestLinks.main_url+"/register")
        random_email = generate_email()
        random_password = generate_password()

        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.REG_NAME)).send_keys(TestUser.name)
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.REG_EMAIL)).send_keys(random_email)
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.REG_PASSWORD)).send_keys(random_password)
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_REG_SUBMIT)).click()
        WDW(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_LOGIN))

        assert  driver.find_element(*Locators.BUTTON_LOGIN).is_displayed()


#Ошибку для некорректного пароля.