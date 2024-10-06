from selenium.webdriver.common.by import By


class BasePageLocators:
    LOADING_MODAL_OVERLAY = [By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"]
    CONSTRUCTOR_BUTTON = [By.XPATH, "//p[text()='Конструктор']/parent::a"]
    ORDER_HISTORY_BUTTON = [By.XPATH, "//p[text()='Лента Заказов']/parent::a"]

