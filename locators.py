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

    #кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = By.XPATH, '//*[contains(text(), "Конструктор")]'

    #кнопка "Оформить заказ"
    BUTTON_MAKE_ORDER = By.XPATH, '//*[contains(text(), "Оформить заказ")]'

    #логотип "Stellar"
    LOGO_STELLAR = By.XPATH, '//*[contains(@class, "AppHeader_header__logo__2D0X2")]'

    #раздел начинки
    BUTTON_STUFFING = By.XPATH, '//*[contains(text(), "Начинки")]'

    # раздел соусы
    BUTTON_SAUCE = By.XPATH, '//*[contains(text(), "Соусы")]'

    # раздел булки
    BUTTON_BREAD = By.XPATH, '//*[contains(text(), "Булки")]'

    #раздел активный
    TAB_ACTIVE = By.XPATH, '//*[contains(@class, "tab_tab_type_current__2BEPc")]'

    #link войти
    LINK_LOGIN = By.XPATH, '//*[contains(@class, "Auth_link__1fOlj")]'

    #name в регистрации
    REG_NAME = By.XPATH, '//label[text()="Имя"]/following-sibling::input'

    #email в регистрации
    REG_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'

    #пароль в регистрации
    REG_PASSWORD = By.XPATH, '//label[text()="Пароль"]/following-sibling::input'

    #кнопка зарегистрироваться
    BUTTON_REG_SUBMIT = By.XPATH,'//*[contains(text(), "Зарегистрироваться")]'

    #ошибка неверный пароль
    TEXT_WRONG_PASSWORD = By.XPATH, '//*[contains(@class, "input__error")]'


