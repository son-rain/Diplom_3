import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step("Открываем историю заказов")
    def click_orders_history(self):
        self.wait_and_find_element(AccountPageLocators.ORDERS_HISTORY_LINK).click()

    @allure.step("Нажимаем на Выход из аккаунта")
    def click_user_logout(self):
        self.wait_and_find_element(AccountPageLocators.LOGOUT_LINK).click()

    @allure.step("Получаем первый ID в списке заказов")
    def get_first_order_id(self):
        return self.wait_and_find_element(AccountPageLocators.FIRST_ORDER_ID).text
