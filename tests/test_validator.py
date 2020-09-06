import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("hanif"))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
