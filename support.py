from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from data import  TestUser
from locators import Locators
import random
import string

def make_login(driver):
    WDW(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_USER_EMAIL)).send_keys(TestUser.email)
    WDW(driver, 5).until(EC.element_to_be_clickable(Locators.INPUT_USER_PASSWORD)).send_keys(TestUser.password)
    WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGIN)).click()
    WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_MAKE_ORDER))

def generate_password():
    random_password = ''.join(random.choices(string.ascii_letters, k=6))
    return random_password

def generate_email():
    random_email = f'evgeny_kovrigin_18_{random.randint(100, 999)}@{''.join(random.choices(string.ascii_lowercase, k=4))}.ru'
    return random_email

