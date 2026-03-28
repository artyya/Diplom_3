from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")

    FLUORESCENT_BUN = (By.XPATH, "//*[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//*[text()='Флюоресцентная булка R2-D3']/ancestor::a//*[contains(@class, 'counter_counter__num')]"
    )

    MODAL_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay')]/parent::div")
    OVERLAY_ANIMATION = (By.XPATH, "//img[@alt='loading animation']")

    BASKET_LIST = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(., 'Оформить заказ')]")

    ORDER_ID = (
        By.XPATH,
        ".//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]"
    )