from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    PWD_FIElD = [By.XPATH, "//label[text()='Пароль']/following::input"]
    PWD_VIS_BUTTON = [By.XPATH, "//div[contains(@class, 'input__icon')]"]
    PWD_FIELD_DIV = [By.XPATH, "//label[text()='Пароль']/parent::div"]

