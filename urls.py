class URL:
    MAIN_PAGE = 'https://stellarburgers.education-services.ru/'
    AUTH_PAGE = f'{MAIN_PAGE}login'
    ORDER_PAGE = f'{MAIN_PAGE}feed'

    REGISTER_USER_URL = f'{MAIN_PAGE}api/auth/register'
    USER_URL = f'{MAIN_PAGE}api/auth/user'
    ORDERS_URL = f'{MAIN_PAGE}api/orders'