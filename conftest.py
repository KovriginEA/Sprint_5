import pytest
from selenium import webdriver
from data import TestUser, TestLinks
from locators import Locators

# Фикстура для вебдрайвера
@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome()
    driver.get(TestLinks.main_url)
    yield driver
    driver.quit()


# Фикстура для авторизация
@pytest.fixture
def login(driver):
    driver.find_element(*Locators.BUTTON_LOGIN_TO_ACCOUNT).click()
    driver.find_element(*Locators.INPUT_USER_EMAIL).send_keys(TestUser.email)
    driver.find_element(*Locators.INPUT_USER_PASSWORD).send_keys(TestUser.password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()