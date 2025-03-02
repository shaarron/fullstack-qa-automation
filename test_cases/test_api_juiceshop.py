import allure
from workflows.api_flows import ApiFlows
from extensions.verifications import Verifications as Verify
from utilities.common_ops import generate_random_string


class TestAPI:

    @allure.title('Test 01: successful registration test')
    @allure.description('positive flow - check registration sanity works')
    def test01_registration_success(self):
        random_email = generate_random_string(10)
        response = ApiFlows.user_creation(
            email=f"{random_email}@gmail.com",
            password="12345678",
            repeated_password="12345678",
            security_question="Mother's maiden name?",
            security_answer="some random name"
        )

        Verify.verify_equals(response.status_code, 201)

    @allure.title('Test 02: email already registered')
    @allure.description('negative flow - check registration attempt with the same email')
    def test02_registration_success(self):
        random_email = generate_random_string(10)
        test_email = f"{random_email}@gmail.com"

        first_creation_response = ApiFlows.user_creation(
            email=test_email,
            password="12345678",
            repeated_password="12345678",
            security_question="Mother's maiden name?",
            security_answer="some random name"
        )

        second_creation_response = ApiFlows.user_creation(
            email=test_email,
            password="12345678",
            repeated_password="12345678",
            security_question="Mother's maiden name?",
            security_answer="some random name"
        )

        Verify.verify_equals(first_creation_response.status_code, 201)
        Verify.verify_equals(second_creation_response.status_code, 400)
