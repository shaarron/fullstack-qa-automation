import random
import string


class DataGeneration:


    @staticmethod
    def generate_random_string(length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

