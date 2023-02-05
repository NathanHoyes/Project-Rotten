import unittest
import sys
sys.path.append("\Project-Rotten\main\src\CredentialsManagement")

from CredentialsHasher import CredentialsHasher

class TestCredentialsHasher(unittest.TestCase):

    def test_should_hash_correctly_test(self):
        hasher = CredentialsHasher()
        value = "test_value_to_be_hashed"
        expected_hashed_value = "4de44895c61874e52d01cbf262906818b48f2d2145772b5281dd0cf7f628cc07"
        hashed_value = hasher.hashValue(value)

        self.assertEqual(hashed_value, expected_hashed_value,
                         f"Incorrect hashed value: Expected {expected_hashed_value} but was {hashed_value}")

    def test_should_not_hash_if_integer_data_type(self):
        hasher = CredentialsHasher()
        value = 15
        expected_value = None
        hashed_value = hasher.hashValue(value)
        self.assertEqual(hashed_value, expected_value,
                         f"Incorrect hashed value: Expected {expected_value} but was {hashed_value}")

    def test_should_not_hash_if_float_data_type(self):
        hasher = CredentialsHasher()
        value = 15.4
        expected_value = None
        hashed_value = hasher.hashValue(value)
        self.assertEqual(hashed_value, expected_value,
                         f"Incorrect hashed value: Expected {expected_value} but was {hashed_value}")

    def test_should_get_correct_hashed_login_token(self):
        hasher = CredentialsHasher()
        expected_hashed_login_token = "47a6f89fde1cc1a83a5d625f51b26c1c7d2a3e45c68d597899d13eb51c29aac2"
        hashed_email = "f359e5ce5ee865e2448c07b69906c99bd3ae0fea22968088174a7eda5ba1dfaa"
        hashed_password = "fd5cb51bafd60f6fdbedde6e62c473da6f247db271633e15919bab78a02ee9eb"
        hashed_login_token = hasher.createHashedLoginToken(hashed_email, hashed_password)
        self.assertEqual(hashed_login_token, expected_hashed_login_token,
                         f"Incorrect hashed value: Expected {expected_hashed_login_token} but was {hashed_login_token}")

unittest.main()
