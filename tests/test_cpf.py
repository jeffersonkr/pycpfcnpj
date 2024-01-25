import unittest

from pycpfcnpj import cpf


class CPFTests(unittest.TestCase):
    """docstring for CPFTests"""

    def setUp(self):
        self.valid_cpf = "11144477735"
        self.masked_valid_cpf = "111.444.777-35"
        self.invalid_cpf = "11144477736"
        self.masked_invalid_cpf = "111.444.777-36"
        self.invalid_cpf_whitespaces = "111444 77735"
        self.invalid_cpf_with_alphabetic = "111444A77735"
        self.invalid_cpf_with_special_character = "*55759997&9"

    def test_validate_cpf_true(self):
        self.assertTrue(cpf.validate(self.valid_cpf))

    def test_validate_masked_cpf_true(self):
        self.assertTrue(cpf.validate(self.masked_valid_cpf))

    def test_validate_cpf_false(self):
        self.assertFalse(cpf.validate(self.invalid_cpf))

    def test_validate_masked_cpf_false(self):
        self.assertFalse(cpf.validate(self.masked_invalid_cpf))

    def test_validate_cpf_with_same_numbers(self):
        for i in range(10):
            self.assertFalse(cpf.validate("{0}".format(i) * 11))

    def test_validate_cpf_unicode_true(self):
        self.assertTrue(cpf.validate("11144477735"))

    def test_validate_cpf_unicode_false(self):
        self.assertFalse(cpf.validate("11144477736"))

    def test_validate_masked_unicode_cpf_true(self):
        self.assertTrue(cpf.validate("111.444.777-35"))

    def test_validate_masked_unicode_cpf_false(self):
        self.assertFalse(cpf.validate("111.444.777-38"))

    def test_validate_cpf_with_whitespaces(self):
        self.assertFalse(cpf.validate(self.invalid_cpf_whitespaces))

    def test_validate_cpf_with_alphabetic_characters(self):
        self.assertFalse(cpf.validate(self.invalid_cpf_with_alphabetic))

    def test_validate_cpf_with_special_characters(self):
        self.assertFalse(cpf.validate(self.invalid_cpf_with_special_character))
