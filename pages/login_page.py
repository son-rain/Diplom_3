import time

import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Переходим на страницу Восстановления пароля")
    def click_pwd_recovery_link(self):
        self.wait_and_find_element(LoginPageLocators.PASSWORD_RECOVERY_LINK).click()
        time.sleep(20)

    @allure.step("Заполняем форму и логинимся пользователем")
    def login_user(self, user_data):
        self.wait_and_find_element(LoginPageLocators.EMAIL_INPUT).send_keys(user_data['email'])
        self.wait_and_find_element(LoginPageLocators.PWD_INPUT).send_keys(user_data['password'])
        self.wait_loading_modal()
        self.wait_and_find_element(LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()

    @allure.step("Ожидаем видимости названия страницы логина")
    def wait_for_login_label(self):
        self.wait_element(LoginPageLocators.LOGIN_LABEL)


