import allure

from urls import URL
from pages.base_page import BasePage
from locators.auth_page_locators import AuthPageLocators
from locators.main_page_locators import MainPageLocators


class AuthPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def open_auth_page(self):
        self.open_page(URL.AUTH_PAGE)

    @allure.step("Авторизоваться")
    def auth(self, email, password):
        self.send_keys_to_field(AuthPageLocators.EMAIL, email)
        self.send_keys_to_field(AuthPageLocators.PASSWORD, password)
        self.wait_for_element_hide(MainPageLocators.OVERLAY_ANIMATION)
        self.click_on_element(AuthPageLocators.LOGIN_BUTTON)