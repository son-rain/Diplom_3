from data import Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage


class Helpers:
    @staticmethod
    def make_order(driver, create_user_data):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.STELLAR_BURGER_LOGIN_URL)
        user_data = create_user_data
        login_page.login_user(user_data)
        main_page = MainPage(driver)
        main_page.wait_loading_modal()
        main_page.add_ingredients_to_basket(driver)
        main_page.click_to_make_order()
        main_page.wait_loading_modal()
        main_page.close_order_modal()
        main_page.wait_loading_modal()
        main_page.click_on_account_button()

    @staticmethod
    def order_id_in_list(id, orders_list):
        order_id = f'0{id}'
        return order_id in orders_list
