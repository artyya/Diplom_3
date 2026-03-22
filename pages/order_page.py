import allure

from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from urls import URL
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Открыть страницу ленты заказов")
    def open_order_page(self):
        self.open_page(URL.ORDER_PAGE)

    @allure.step("Проверить, что страница ленты заказов открыта")
    def is_order_page_opened(self):
        return self.get_current_url() == URL.ORDER_PAGE

    @allure.step("Дождаться загрузки страницы ленты заказов")
    def wait_for_feed_page_open(self):
        self.wait_for_element_visible(OrderPageLocators.FEED_TITLE)
        self.wait_for_element_visible(OrderPageLocators.TOTAL_ORDERS)
        self.wait_for_element_visible(OrderPageLocators.IN_PROGRESS_SECTION)

    @allure.step("Дождаться загрузки страницы ленты заказов")
    def wait_for_order_page_to_load(self):
        self.wait_for_feed_page_open()

    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_total_orders_count(self):
        count = self.get_text_of_element(OrderPageLocators.TOTAL_ORDERS)
        return int(count)

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        count = self.get_text_of_element(OrderPageLocators.TODAY_ORDERS)
        return int(count)

    @allure.step("Получить номера заказов из блока 'В работе'")
    def get_in_progress_numbers(self):
        elements = self.driver.find_elements(*OrderPageLocators.IN_PROGRESS_NUMBERS)
        return [int(element.text.strip()) for element in elements]

    @allure.step("Дождаться увеличения счётчика 'Выполнено за всё время'")
    def wait_until_total_changes(self, start_value):
        WebDriverWait(self.driver, 30, poll_frequency=1).until(
            lambda driver: self._refresh_and_get_total() > start_value
        )

    @allure.step("Дождаться увеличения счётчика 'Выполнено за сегодня'")
    def wait_until_today_changes(self, start_value):
        WebDriverWait(self.driver, 30, poll_frequency=1).until(
            lambda driver: self._refresh_and_get_today() > start_value
        )

    @allure.step("Дождаться появления номера заказа в блоке 'В работе'")
    def wait_until_order_in_progress(self, order_number):
        WebDriverWait(self.driver, 20, poll_frequency=0.5).until(
            lambda driver: int(order_number) in self.get_in_progress_numbers()
        )

    def _refresh_and_get_total(self):
        self.driver.refresh()
        self.wait_for_feed_page_open()
        return self.get_total_orders_count()

    def _refresh_and_get_today(self):
        self.driver.refresh()
        self.wait_for_feed_page_open()
        return self.get_today_orders_count()