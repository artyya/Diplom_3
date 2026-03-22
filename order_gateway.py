import requests

from urls import URL


class OrderGateway:
    def __init__(self, token):
        self.headers = {"Authorization": token}
        self.payload = {
            "ingredients": [
                "61c0c5a71d1f82001bdaaa6d",
                "61c0c5a71d1f82001bdaaa73",
                "61c0c5a71d1f82001bdaaa70"
            ]
        }

    def create_order(self):
        response = requests.post(URL.ORDERS_URL, json=self.payload, headers=self.headers)
        return response.json()["order"]["number"]