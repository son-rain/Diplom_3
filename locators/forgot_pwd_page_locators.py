from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL_FIElD = [By.XPATH, "//label[text()='Email']/following::input"]
    SUBMIT_RESET_PWD_BUTTON = [By.XPATH, "//button[text()='Восстановить']"]
