import allure

import data
from pages.forgot_pwd_page import ForgotPasswordPage
from pages.login_page import LoginPage
from data import Urls
from pages.reset_pwd_page import ResetPasswordPage


class TestPasswordRecovery:
    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_move_to_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.STELLAR_BURGER_LOGIN_URL)

        login_page.click_pwd_recovery_link()

        forgot_pwd_page = ForgotPasswordPage(driver)
        assert forgot_pwd_page.get_current_url() == Urls.STELLAR_BURGER_FORGOTTEN_PWD_URL

    @allure.title("Проверка ввода почты и клика по кнопке «Восстановить»")
    def test_recover_pwd(self, driver):
        forgot_pwd_page = ForgotPasswordPage(driver)
        forgot_pwd_page.open_page(Urls.STELLAR_BURGER_FORGOTTEN_PWD_URL)
        forgot_pwd_page.fill_email_field('ya@ya.ru')
        forgot_pwd_page.submit_reset_pwd_form()

        reset_pwd_page = ResetPasswordPage(driver)
        reset_pwd_page.wait_for_reset_pwd_field()
        assert reset_pwd_page.get_current_url() == Urls.STELLAR_BURGER_RESET_PWD_URL

    @allure.title("Проверка ввода почты и клика по кнопке «Восстановить»")
    def test_pwd_visibility(self, driver):
        forgot_pwd_page = ForgotPasswordPage(driver)
        forgot_pwd_page.open_page(Urls.STELLAR_BURGER_FORGOTTEN_PWD_URL)
        forgot_pwd_page.fill_email_field(data.TextData.EMAIL)
        forgot_pwd_page.submit_reset_pwd_form()
        reset_pwd_page = ResetPasswordPage(driver)
        reset_pwd_page.wait_for_reset_pwd_field()
        reset_pwd_page.fill_pwd_field(data.TextData.PWD)
        reset_pwd_page.wait_loading_modal()
        reset_pwd_page.click_on_eye_button()
        assert reset_pwd_page.pwd_field_is_active() is True
