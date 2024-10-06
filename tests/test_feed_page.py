import time

import allure

from helpers import Helpers as helpers
from data import Urls
from pages.account_page import AccountPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestFeedPage:
    @allure.title("Проверка, если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_order_details_modal(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_page(Urls.STELLAR_BURGER_FEED_URL)
        order_name = feed_page.click_on_first_order_in_feed_and_get_text()
        modal_order_name = feed_page.get_orderbox_text()
        assert order_name == modal_order_name

    @allure.title("Проверка, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_users_orders_in_feed(self, driver, create_user_data):
        helpers.make_order(driver, create_user_data)
        account_page = AccountPage(driver)
        account_page.wait_loading_modal()
        account_page.click_orders_history()
        history_first_order_id = account_page.get_first_order_id()

        feed_page = FeedPage(driver)
        feed_page.click_on_order_history_button()
        feed_order_id_list = feed_page.get_order_id_list()
        assert history_first_order_id in feed_order_id_list

    @allure.title("Проверка, при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_order_number_increased_in_done_for_all_time(self, driver, create_user_data):
        feed_page = FeedPage(driver)
        feed_page.open_page(Urls.STELLAR_BURGER_FEED_URL)
        initial_number_of_orders = feed_page.get_order_number_for_all_time()
        helpers.make_order(driver, create_user_data)
        feed_page.wait_loading_modal()
        feed_page.click_on_order_history_button()
        actual_number_of_orders = feed_page.get_order_number_for_all_time()
        assert actual_number_of_orders > initial_number_of_orders

    @allure.title("Проверка, при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_order_number_increased_in_done_for_today(self, driver, create_user_data):
        feed_page = FeedPage(driver)
        feed_page.open_page(Urls.STELLAR_BURGER_FEED_URL)
        initial_number_of_orders = feed_page.get_order_number_for_today()
        helpers.make_order(driver, create_user_data)
        feed_page.wait_loading_modal()
        feed_page.click_on_order_history_button()
        actual_number_of_orders = feed_page.get_order_number_for_today()
        assert actual_number_of_orders > initial_number_of_orders

    @allure.title("Проверка, что после оформления заказа его номер появляется в разделе В работе")
    def test_order_id_display_in_orders_in_progress(self, driver, create_user_data):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.STELLAR_BURGER_LOGIN_URL)
        user_data = create_user_data
        login_page.login_user(user_data)
        main_page = MainPage(driver)
        main_page.wait_loading_modal()
        main_page.add_ingredients_to_basket(driver)
        main_page.click_to_make_order()
        main_page.wait_loading_modal()
        order_id = main_page.get_modal_order_id()
        main_page.close_order_modal()
        main_page.wait_loading_modal()
        main_page.click_on_order_history_button()
        feed_page = FeedPage(driver)
        feed_page.wait_for_feed_page_title()
        orders_list = feed_page.get_order_id_in_progress_list()
        assert helpers.order_id_in_list(order_id, orders_list) is True















