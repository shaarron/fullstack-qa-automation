class ApiData:
    @staticmethod
    def user_creation_payload(email, password, repeated_password, security_question, security_answer):
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
        return payload
