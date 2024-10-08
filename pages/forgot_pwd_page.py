import allure

from pages.base_page import BasePage
from locators.forgot_pwd_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):

    @allure.step("Заполняем поле email")
    def fill_email_field(self, text):
        email_input = self.wait_and_find_element(ForgotPasswordPageLocators.EMAIL_FIElD)
        email_input.send_keys(text)

    @allure.step("Подтверждаем запрос на сброс пароля")
    def submit_reset_pwd_form(self):
        self.wait_and_find_element(ForgotPasswordPageLocators.SUBMIT_RESET_PWD_BUTTON).click()


