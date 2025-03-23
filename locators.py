from selenium.webdriver.common.by import By

class Locators:
    #"Войти в аккаунт" на главной
    BUTTON_LOGIN_TO_ACCOUNT = By.XPATH, './/button[text() = "Войти в аккаунт"]'

    #поле имя
    INPUT_USERNAME = By.XPATH, '//label[text()="Имя"]/following-sibling::input'

    #поле Email
    INPUT_USER_EMAIL = By.XPATH, './/label[text()="Email"]/following-sibling::input'

    #поле "Пароль"
    INPUT_USER_PASSWORD = By.XPATH, './/input[@name="Пароль"]'

    #"Войти" кнопка
    BUTTON_LOGIN = By.XPATH, '//button[text()="Войти"]'

    #кнопка "Личный Кабинет"
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, '//p[text() = "Личный Кабинет"]'

    #кнопка "Выйти"
    BUTTON_LOGOUT = By.XPATH, '//*[contains(text(), "Выход")]'

    #Профиль
    TEXT_PROFILE = By.XPATH, '//*[contains(text(), "Профиль")]'