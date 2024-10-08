from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_PAGE_TITLE = [By.XPATH, '//h1[text()="Лента заказов"]']
    ORDER_HISTORY_ITEM = [By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]//h2[contains (@class, "text")]']
    MODAL_ORDERBOX = [By.XPATH, '//div[contains(@class, "Modal_orderBox")]/h2[contains(@class, "text")]']
    ORDER_ID = [By.XPATH, '//p[starts-with (text(), "#")]']
    ORDER_NUMBER_ALL_TIME = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "OrderFeed_number")]']
    ORDER_NUMBER_TODAY = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "OrderFeed_number")]']
    ORDER_ID_LIST_IN_PROGRESS = [By.XPATH, '//ul[contains (@class, "OrderFeed_orderListReady")]/li']
    FIRST_ORDER_ID_IN_LIST_IN_PROGRESS = [By.XPATH, '//ul[contains (@class, "OrderFeed_orderListReady")]/li[1]']
