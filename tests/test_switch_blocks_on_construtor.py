from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from data import  TestLinks
from locators import Locators

class TestSwitchBlockssOnConstructor:
    #переход в начинки
    def test_switch_blocks_to_stuffing(self, driver):
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_STUFFING)).click()
        assert driver.find_element(*Locators.TAB_ACTIVE).text == 'Начинки'

    #переход в соусы
    def test_switch_blocks_to_sauce(self, driver):
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_SAUCE)).click()
        assert driver.find_element(*Locators.TAB_ACTIVE).text == 'Соусы'

    # переход в булки из соусов
    def test_switch_blocks_to_bread_from_sauce(self, driver):
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_SAUCE)).click()
        WDW(driver, 5).until(EC.visibility_of_element_located(Locators.TAB_ACTIVE))
        WDW(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_BREAD)).click()
        assert driver.find_element(*Locators.TAB_ACTIVE).text == 'Булки'

