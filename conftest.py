import pytest
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from helpers import normalize_token
from pages.auth_page import AuthPage
from urls import URL
from generators import generate_user_data


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver_instance = webdriver.Chrome(service=service)
    else:
        driver_instance = webdriver.Firefox()

    driver_instance.maximize_window()
    driver_instance.get(URL.MAIN_PAGE)

    yield driver_instance

    driver_instance.quit()


@pytest.fixture(scope="function")
def create_and_delete_user():
    user_data = generate_user_data()

    register_response = requests.post(URL.REGISTER_USER_URL, json=user_data)
    access_token = normalize_token(register_response.json()["accessToken"])

    user_data["token"] = access_token

    yield user_data

    headers = {"Authorization": user_data["token"]}
    requests.delete(URL.USER_URL, headers=headers)


@pytest.fixture(scope="function")
def login_user(driver, create_and_delete_user):
    auth_page = AuthPage(driver)
    auth_page.open_auth_page()
    auth_page.auth(
        create_and_delete_user["email"],
        create_and_delete_user["password"]
    )
    return driver