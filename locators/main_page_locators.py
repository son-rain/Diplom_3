from selenium.webdriver.common.by import By

from data import BurgerData


class MainPageLocators:
    ACCOUNT_BUTTON = [By.XPATH, "//a/p[text()='Личный Кабинет']"]
    BURGER_BUN = [By.XPATH, f"//p[contains (text(), '{BurgerData.BUN_NAME}')]/parent::a"]
    BURGER_SAUCE = [By.XPATH, f"//p[contains (text(), '{BurgerData.SAUCE_NAME}')]/parent::a"]
    BURGER_FILLING = [By.XPATH, f"//p[contains (text(), '{BurgerData.FILLING_NAME}')]/parent::a"]
    INGREDIENT_DETAILS_MODAL = [By.XPATH, "//h2[text()='Детали ингредиента']/ancestor::section[contains(@class, 'Modal')]"]
    INGREDIENT_DETAILS_MODAL_X_BUTTON = [By.XPATH, "//button[contains (@class, 'modal__close')]"]
    BASKET = [By.XPATH, "//ul[contains (@class, 'BurgerConstructor_basket__list')]"]
    BURGER_BUN_INGREDIENT_COUNTER = [By.XPATH, f"//p[contains (text(), '{BurgerData.BUN_NAME}')]/parent::a/div[contains (@class, 'counter')]"]
    MAKE_ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"]
    ORDER_ID_LABEL = [By.XPATH, "//p[text()='идентификатор заказа']"]
    TICK_ANIMATION = [By.XPATH, "//img[contains (@alt, 'tick animation')]"]
    ORDER_MODAL = [By.XPATH, "//p[text()='идентификатор заказа']/ancestor::section[contains(@class, 'Modal')]"]
    ORDER_MODAL_X_BUTTON = [By.XPATH, '//div[contains (@class,"Modal_modal__container__Wo2l_")]/button[contains(@class, "modal__close")]']
    ORDER_MODAL_ID_TEXT = [By.XPATH, '//p[text()="идентификатор заказа"]/preceding-sibling::h2[contains(@class, "modal__title")]']

