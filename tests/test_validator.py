import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):

    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("hanif"))

    def test_validate_name_with_invalid_string_int_input(self):
        self.assertEqual(False, validate_name("1234"))

    def test_validate_name_with_invalid_input_contain_string_of_int(self):
        self.assertEqual(False, validate_name("aaa122"))

    # def test_validate_name_with_invalid_input_lang_thai(self):
    #     self.assertEqual(False, validate_name("กกกกกก"))

    def test_validate_name_with_invalid_input_special_char(self):
        self.assertEqual(False, validate_name("ff_**"))

    def test_validate_name_with_invalid_input_special_char2(self):
        self.assertEqual(False, validate_name("'!*/-+$%#@"))

    def test_validate_name_with_invalid_input_special_char3(self):
        self.assertEqual(False, validate_name("'!*/-+อะไรกันครับเนี่ย $%#@"))

    def test_validate_name_with_invalid_input_empty_string(self):
        self.assertEqual(False, validate_name(" "))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
