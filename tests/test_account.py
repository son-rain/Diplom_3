import allure

from data import Urls
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestAccountPage:
    @allure.title("Проверка перехода по клику на «Личный кабинет» без авторизации")
    def test_account_page_availability_noauth(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.STELLAR_BURGER_URL)

        main_page.click_on_account_button()
        assert main_page.get_current_url() == Urls.STELLAR_BURGER_LOGIN_URL

    def test_orders_history(self, driver, create_user_data):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.STELLAR_BURGER_LOGIN_URL)
        user_data = create_user_data
        login_page.login_user(user_data)

        main_page = MainPage(driver)
        main_page.wait_loading_modal()
        main_page.click_on_account_button()

        account_page = AccountPage(driver)
        account_page.wait_loading_modal()
        account_page.click_orders_history()
        assert account_page.get_current_url() == Urls.STELLAR_BURGER_ORDER_HISTORY_URL

    @allure.title("Проверка выхода из аккаунта")
    def test_user_logout(self, driver, create_user_data):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.STELLAR_BURGER_LOGIN_URL)
        user_data = create_user_data
        login_page.login_user(user_data)

        main_page = MainPage(driver)
        main_page.wait_loading_modal()
        main_page.click_on_account_button()

        account_page = AccountPage(driver)
        account_page.wait_loading_modal()
        account_page.click_user_logout()
        account_page.wait_loading_modal()
        login_page.wait_for_login_label()
        assert login_page.get_current_url() == Urls.STELLAR_BURGER_LOGIN_URL




