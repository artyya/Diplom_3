from selenium.webdriver.common.by import By


class OrderPageLocators:
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    IN_PROGRESS_SECTION = (
        By.XPATH,
        "//p[text()='В работе:']/following-sibling::ul[1]"
    )

    IN_PROGRESS_NUMBERS = (
        By.XPATH,
        "//p[text()='В работе:']/following-sibling::ul[1]//li[contains(@class, 'text_type_digits-default')]"
    )