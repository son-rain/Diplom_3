import allure

from locators.reset_pwd_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step("Ожидаем появления поля для сброса пароля")
    def wait_for_reset_pwd_field(self):
        self.wait_element(ResetPasswordPageLocators.PWD_FIElD)

    @allure.step("Заполняем поле пароля")
    def fill_pwd_field(self, text):
        email_input = self.wait_and_find_element(ResetPasswordPageLocators.PWD_FIElD)
        email_input.send_keys(text)

    @allure.step("Ожидаем появления переключателя видимости пароля")
    def wait_for_eye_button(self):
        self.wait_element(ResetPasswordPageLocators.PWD_VIS_BUTTON)

    @allure.step("Нажимаем на переключатель видимости пароля")
    def click_on_eye_button(self):
        self.wait_and_find_element(ResetPasswordPageLocators.PWD_VIS_BUTTON).click()

    @allure.step("Проверяем что поля для пароля подстветилось")
    def pwd_field_is_active(self):
        pwd_input_div = self.wait_and_find_element(ResetPasswordPageLocators.PWD_FIELD_DIV)
        return "input_status_active" in pwd_input_div.get_attribute("class")

