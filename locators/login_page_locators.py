from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD_RECOVERY_LINK = [By.XPATH, '//a[contains (@class, "Auth_link_") and text()="Восстановить пароль"]']

    # Поле для ввода email
    EMAIL_INPUT = [By.XPATH, "//label[text()='Email']/following::input"]

    # Поле для ввода пароля
    PWD_INPUT = [By.XPATH, "//label[text()='Пароль']/following::input"]

    LOGIN_SUBMIT_BUTTON = [By.XPATH, '//button[text()="Войти"]']
    LOGIN_LABEL = [By.XPATH, '//div[contains(@class, "login")]/h2[text()="Вход"]']
