import allure
import requests

header = {'Content-Type': 'application/json'}


class ApiActions:

    @staticmethod
    @allure.step('Post request')
    def post(path, payload):
        response = requests.post(path, json=payload, headers=header)
        return response
