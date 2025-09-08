from selenium.webdriver.common.by import By


class Locators:
    BUTTON_ENTER_TO_ACCOUNT = By.XPATH, './/button[contains(text(), "Войти в аккаунт")]'  # кнопка входа в аккаунт
    TEXT_ENTER              = By.XPATH, './/h2[text()="Вход"]'  # Надпись "Вход"
    TITLE_REGISTRATION      = By.XPATH, './/h2[text()="Регистрация"]'  # "текст регистрация"
    BUTTON_REGISTRATION     = By.XPATH, './/button[contains(text(), "Зарегистрироваться")]'  # кнопка зарегистрироваться
    NAME_EMAIL_FIELD        = By.XPATH, './/input[@name="name"]'  # Поля ввода "Имя/Email"
    PASSWORD_FIELD          = By.XPATH, './/input[@name="Пароль"]'  # Поле ввода "Пароль"
    INCORRECT_PASSWORD_TEXT = By.XPATH, './/p[contains(text(), "Некорректный пароль")]'
    BUTTON_ENTER            = By.XPATH, './/button[contains(text(), "Войти")]'  # кнопка входа на странице login
    BUTTON_PLACE_ORDER      = By.XPATH, './/button[contains(text(), "Оформить заказ")]'  # кнопка оформления заказа
    BUILD_BURGER_TEXT       = By.XPATH, './/h1[text()="Соберите бургер"]'  # надпись на странице конструктора
    PERSONAL_AREA           = By.XPATH, './/p[text()="Личный Кабинет"]'  # Кнопка перехода личного кабинета
    ENTER_LINK              = By.XPATH, './/a[text()="Войти"]'  # ссылка "войти" на странице восстановления пароля и регистрации
    TEXT_FROM_PROFILE       = By.XPATH, './/p[text()="В этом разделе вы можете изменить свои персональные данные"]'
    CONSTRUCTOR_BUTTON      = By.XPATH, './/p[text() = "Конструктор"]'  # кнопка констуктор
    BUTTON_MAIN_LOGO        = By.XPATH, './/a[@href = "/"]'  # кнопка с лого для перехода в корень сайта
    BUTTON_BUNS             = By.XPATH, './/span[text()="Булки"]'  # кнопка "Булки" в меню конструктора
    BUTTON_SAUCES           = By.XPATH, './/span[text()="Соусы"]'  # кнопка "Соусы" в меню конструктора
    BUTTON_FILLINGS         = By.XPATH, './/span[text()="Начинки"]'  # кнопка "Начинки" в меню конструктора
    BUTTON_EXIT             = By.XPATH, './/button[text() = "Выход"]'  # кнопка выход в личном кабинете
    ELEMENTS_PARENT         = By.XPATH, '..'  # родитель элемента
