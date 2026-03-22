import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Подождать видимость элемента")
    def wait_for_element_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Подождать кликабельность элемента")
    def wait_for_element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Подождать исчезновение элемента")
    def wait_for_element_hide(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    @allure.step("Получить текст элемента")
    def get_text_of_element(self, locator):
        return self.wait_for_element_visible(locator).text

    @allure.step("Проверить, что элемент отображается")
    def is_element_visible(self, locator):
        return self.wait_for_element_visible(locator).is_displayed()

    @allure.step("Ввести текст в поле")
    def send_keys_to_field(self, locator, text, timeout=20):
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Перетащить элемент")
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Подождать текст в атрибуте")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )