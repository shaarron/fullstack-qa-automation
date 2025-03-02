import allure
from extensions.api_actions import ApiActions


class ApiFlows:

    @staticmethod
    @allure.step('create user via api call')
    def user_creation(email, password, repeated_password, security_question, security_answer):
        path = 'https://juice-shop.herokuapp.com/api/Users/'
        payload = {
            "email": email,
            "password": password,
            "passwordRepeat": repeated_password,
            "securityQuestion": {
                "id": 2,
                "question": security_question
            },
            "securityAnswer": security_answer
        }

        response = ApiActions.post(path=path, payload=payload)
        return response
