import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from seletools.actions import drag_and_drop


class MainPage(BasePage):
    @allure.step("Переходим в личный кабинет")
    def click_on_account_button(self):
        self.wait_and_find_element(MainPageLocators.ACCOUNT_BUTTON).click()

    @allure.step("Кликаем по ингредиенту")
    def click_on_ingredient(self):
        self.wait_and_find_element(MainPageLocators.BURGER_BUN).click()

    @allure.step("Проверяем видимость окна с ингредиентами")
    def modal_ingredient_details_is_displayed(self):
        return "opened" in self.wait_and_find_element(MainPageLocators.INGREDIENT_DETAILS_MODAL).get_attribute("class")

    @allure.step("Закрываем модальное окно с ингредиентами")
    def close_modal_modal_ingredient_details(self):
        self.wait_and_find_element(MainPageLocators.INGREDIENT_DETAILS_MODAL_X_BUTTON).click()

    @allure.step("Проверяем закрытие окна с ингредиентами")
    def modal_ingredient_details_is_closed(self):
        return "opened" not in self.wait_element_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL).get_attribute("class")

    @allure.step("Находим булку на странице")
    def get_one_bun(self):
        return self.wait_and_find_element(MainPageLocators.BURGER_BUN)

    @allure.step("Читаем значение каунтера ингредиента")
    def get_ingredient_number(self):
        counter = self.wait_and_find_element(MainPageLocators.BURGER_BUN_INGREDIENT_COUNTER).text
        return counter

    @allure.step("Добавляем булку в корзину")
    def add_bun_to_basket(self, driver, locator):
        bun = locator
        basket = self.wait_and_find_element(MainPageLocators.BASKET)
        drag_and_drop(driver, bun, basket)

    @allure.step("Добавляем список ингредиентов в корзину")
    def add_ingredients_to_basket(self, driver):
        bun = self.wait_and_find_element(MainPageLocators.BURGER_BUN)
        sauce = self.wait_and_find_element(MainPageLocators.BURGER_SAUCE)
        filling = self.wait_and_find_element(MainPageLocators.BURGER_FILLING)
        basket = self.wait_and_find_element(MainPageLocators.BASKET)

        for item in [bun, sauce, filling]:
            drag_and_drop(driver, item, basket)

    @allure.step("Оформляем заказ")
    def click_to_make_order(self):
        self.wait_and_find_element(MainPageLocators.MAKE_ORDER_BUTTON).click()

    @allure.step("Проверяем видимость окна с деталями заказа")
    def modal_order_details_is_open(self):
        return "opened" in self.wait_and_find_element(MainPageLocators.ORDER_MODAL).get_attribute("class")

    @allure.step("Закрываем окно с деталями заказа")
    def close_order_modal(self):
        self.wait_and_find_element(MainPageLocators.ORDER_MODAL_X_BUTTON).click()

    @allure.step("Получаем id заказа из окна заказа")
    def get_modal_order_id(self):
        return self.wait_and_find_element(MainPageLocators.ORDER_MODAL_ID_TEXT).text
