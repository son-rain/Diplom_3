import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Находим элемент на странице и ожидаем его видимости")
    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Ожидаем видимости элемента на странице")
    def wait_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ожидаем невидимости элемента на странице")
    def wait_element_invisible(self, locator):
        WebDriverWait(self.driver, 30).until_not(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Скроллим к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Читаем текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Открываем страницу")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Ожидаем модальное окно")
    def wait_loading_modal(self):
        self.wait_element_invisible(BasePageLocators.LOADING_MODAL_OVERLAY)

    @allure.step("Кликаем на ссылку Конструктора")
    def click_on_constructor_button(self):
        self.wait_and_find_element(BasePageLocators.CONSTRUCTOR_BUTTON).click()

    @allure.step("Открываем Ленту Заказов")
    def click_on_order_history_button(self):
        self.wait_and_find_element(BasePageLocators.ORDER_HISTORY_BUTTON).click()

    @allure.step("Получаем список элементов")
    def get_elements_list(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        list = self.driver.find_elements(*locator)
        return list

    @allure.step("Ожидаем элемент без указанного текста")
    def wait_for_list_without_text(self, locator, text):
        WebDriverWait(self.driver, 30).until_not(expected_conditions.text_to_be_present_in_element(locator, text))



