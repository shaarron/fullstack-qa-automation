import allure
from extensions.api_actions import ApiActions
from extensions.api_data import ApiData


class ApiFlows:
    @staticmethod
    @allure.step('create user via api call')
    def user_creation(email, password, repeated_password, security_question, security_answer):
        path = 'https://juice-shop.herokuapp.com/api/Users/'
        api_data = ApiData()
        user_data_payload = api_data.user_creation_payload(email=email, password=password,
                                                           repeated_password=repeated_password,
                                                           security_question=security_question,
                                                           security_answer=security_answer)
        response = ApiActions.post(path=path, payload=user_data_payload)
        return response
