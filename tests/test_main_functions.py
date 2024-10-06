import time

import allure

from data import Urls
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainFunctions:
    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_move_to_constructor_page(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_page(Urls.STELLAR_BURGER_FEED_URL)
        feed_page.wait_for_feed_page_title()
        feed_page.click_on_constructor_button()
        feed_page.wait_loading_modal()
        assert feed_page.get_current_url() == Urls.STELLAR_BURGER_URL

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    def test_move_to_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.STELLAR_BURGER_URL)
        main_page.click_on_order_history_button()

        feed_page = FeedPage(driver)
        assert feed_page.feed_title_is_displayed() is True

    @allure.title("Проверка если кликнуть на ингредиент, появится всплывающее окно с деталями»")
    def test_ingredient_modal_is_displayed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.STELLAR_BURGER_URL)
        main_page.click_on_ingredient()
        assert main_page.modal_ingredient_details_is_displayed() is True

    @allure.title("Проверка что всплывающее окно закрывается кликом по крестику»")
    def test_modal_closed_by_click_on_x(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.STELLAR_BURGER_URL)
        main_page.click_on_ingredient()
        main_page.close_modal_modal_ingredient_details()
        assert main_page.modal_ingredient_details_is_closed() is True

    @allure.title("Проверка - при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента»")
    def test_add_ingredient_to_basket(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.STELLAR_BURGER_URL)
        bun = main_page.get_one_bun()
        bun_number = main_page.get_ingredient_number()
        main_page.add_bun_to_basket(driver, bun)
        bun_number2 = main_page.get_ingredient_number()
        assert bun_number < bun_number2

    @allure.title("Проверка что залогиненный пользователь может оформить заказ")
    def test_make_order_with_auth_user(self, driver, create_user_data):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.STELLAR_BURGER_LOGIN_URL)
        user_data = create_user_data
        login_page.login_user(user_data)

        main_page = MainPage(driver)
        main_page.wait_loading_modal()

        main_page.add_ingredients_to_basket(driver)

        main_page.click_to_make_order()
        assert main_page.modal_order_details_is_open() is True







