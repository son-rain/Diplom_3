import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step("Ожидаем появления названия страницы Ленты Заказов")
    def wait_for_feed_page_title(self):
        self.wait_element(FeedPageLocators.FEED_PAGE_TITLE)

    @allure.step("Открываем видимости названия страницы Лента Заказов")
    def feed_title_is_displayed(self):
        return self.wait_and_find_element(FeedPageLocators.FEED_PAGE_TITLE).is_displayed()

    @allure.step("Кликаем по первому заказу в списке и возвращаем его id")
    def click_on_first_order_in_feed_and_get_text(self):
        item = self.wait_and_find_element(FeedPageLocators.ORDER_HISTORY_ITEM)
        item_text = item.text
        item.click()
        return item_text

    @allure.step("Читаем id заказа из модального окна заказа")
    def get_orderbox_text(self):
        return self.wait_and_find_element(FeedPageLocators.MODAL_ORDERBOX).text

    @allure.step("Получаем список заказов")
    def get_order_id_list(self):
        orders_list = self.get_elements_list(FeedPageLocators.ORDER_ID)
        id_list = []
        for matched_element in orders_list:
            text = matched_element.text
            id_list.append(text)
        return id_list

    @allure.step("Получаем кол-во заказов за всё время")
    def get_order_number_for_all_time(self):
        order_number = self.wait_and_find_element(FeedPageLocators.ORDER_NUMBER_ALL_TIME).text
        return order_number

    @allure.step("Получаем кол-во заказов за сегодня")
    def get_order_number_for_today(self):
        order_number = self.wait_and_find_element(FeedPageLocators.ORDER_NUMBER_TODAY).text
        return order_number

    @allure.step("Ождиаем поступления заказа в работу и читаем список заказов")
    def get_order_id_in_progress_list(self):
        id_list = []
        self.wait_for_list_without_text(FeedPageLocators.FIRST_ORDER_ID_IN_LIST_IN_PROGRESS, "Все текущие заказы готовы!")
        orders_list = self.get_elements_list(FeedPageLocators.ORDER_ID_LIST_IN_PROGRESS)
        for matched_element in orders_list:
            text = matched_element.text
            if text == "Все текущие заказы готовы!":
                continue
            id_list.append(text)
        return id_list



