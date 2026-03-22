import allure

from selenium.webdriver.support.ui import WebDriverWait

from urls import URL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(URL.MAIN_PAGE)

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_page_to_load(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY, timeout=20)

    @allure.step("Проверить, что главная страница открыта")
    def is_main_page_opened(self):
        return self.get_current_url() == URL.MAIN_PAGE

    @allure.step("Подождать закрытие оверлея")
    def wait_for_overlay_close(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY, timeout=20)

    @allure.step("Кликнуть на Конструктор")
    def click_on_constructor_button(self):
        self.wait_for_overlay_close()
        self.scroll_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на Ленту заказов")
    def click_on_feed_button(self):
        self.wait_for_overlay_close()
        self.click_on_element(MainPageLocators.FEED_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_on_ingredient(self):
        self.scroll_to_element(MainPageLocators.FLUORESCENT_BUN)
        self.click_on_element(MainPageLocators.FLUORESCENT_BUN)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_on_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_element_hide(MainPageLocators.MODAL_WINDOW)

    @allure.step("Проверить, что модальное окно отображается")
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.MODAL_WINDOW)

    @allure.step("Проверить, что модальное окно закрылось")
    def is_modal_closed(self):
        return self.wait_for_element_hide(MainPageLocators.MODAL_WINDOW)

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter(self):
        count = self.get_text_of_element(MainPageLocators.INGREDIENT_COUNTER)
        return int(count)

    @allure.step("Перетащить булку в корзину")
    def drag_ingredient_bun_to_basket(self):
        self.wait_for_overlay_close()
        self.scroll_to_element(MainPageLocators.FLUORESCENT_BUN)

        source = self.wait_for_element_visible(MainPageLocators.FLUORESCENT_BUN)
        target = self.wait_for_element_visible(MainPageLocators.BASKET_LIST)
        self.drag_and_drop_element(source, target)

        WebDriverWait(self.driver, 10).until(
            lambda driver: int(driver.find_element(*MainPageLocators.INGREDIENT_COUNTER).text) > 0
        )

    @allure.step("Оформить заказ")
    def place_order(self):
        self.wait_for_overlay_close()
        self.wait_for_element_hide(MainPageLocators.OVERLAY_ANIMATION)

        order_button = self.wait_for_element_clickable(MainPageLocators.ORDER_BUTTON, timeout=20)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
        order_button.click() 

    @allure.step("Получить реальный номер заказа")
    def get_order_number(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY_ANIMATION)
        self.wait_for_element_visible(MainPageLocators.ORDER_ID)

        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.find_element(*MainPageLocators.ORDER_ID).text != "9999"
        )

        order_number = self.get_text_of_element(MainPageLocators.ORDER_ID)
        return int(order_number)