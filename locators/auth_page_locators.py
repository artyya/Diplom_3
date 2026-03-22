from selenium.webdriver.common.by import By


class AuthPageLocators:
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")