from selenium.webdriver.common.by import By


class AccountPageLocators:
    ORDERS_HISTORY_LINK = [By.XPATH, "//a[text()='История заказов']"]
    LOGOUT_LINK = [By.XPATH, "//button[text()='Выход']"]
    FIRST_ORDER_ID = [By.XPATH, '//p[contains (@class, "digits-default")][1]']