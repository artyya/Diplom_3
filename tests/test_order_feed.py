import allure

from order_gateway import OrderGateway
from pages.order_page import OrderPage


@allure.feature("Раздел «Лента заказов»")
class TestOrderFeed:

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается после создания нового заказа")
    def test_total_orders_counter_increases_after_creating_order(self, driver, create_and_delete_user):
        order_page = OrderPage(driver)
        order_gateway = OrderGateway(create_and_delete_user["token"])

        order_page.open_order_page()
        order_page.wait_for_feed_page_open()
        start_total = order_page.get_total_orders_count()

        order_gateway.create_order()

        order_page.wait_until_total_changes(start_total)
        finish_total = order_page.get_total_orders_count()

        assert finish_total > start_total

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после создания нового заказа")
    def test_today_orders_counter_increases_after_creating_order(self, driver, create_and_delete_user):
        order_page = OrderPage(driver)
        order_gateway = OrderGateway(create_and_delete_user["token"])

        order_page.open_order_page()
        order_page.wait_for_feed_page_open()
        start_today = order_page.get_today_orders_count()

        order_gateway.create_order()

        order_page.wait_until_today_changes(start_today)
        finish_today = order_page.get_today_orders_count()

        assert finish_today > start_today

    @allure.title("Номер нового заказа появляется в блоке 'В работе'")
    def test_order_number_appears_in_in_progress_section(self, driver, create_and_delete_user):
        order_page = OrderPage(driver)
        order_gateway = OrderGateway(create_and_delete_user["token"])

        order_number = order_gateway.create_order()

        order_page.open_order_page()
        order_page.wait_for_feed_page_open()
        order_page.wait_until_order_in_progress(order_number)

        in_progress_numbers = order_page.get_in_progress_numbers()

        assert int(order_number) in in_progress_numbers