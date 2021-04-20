import unittest
from vigenere import VigenereCipher


class VigenereTestCase(unittest.TestCase):
    def setUp(self):
        self.cipher = VigenereCipher("TRAIN")

    def test_init(self):
        self.assertEqual(self.cipher.keyword, "TRAIN")

    def test_combine_characer(self):
        self.assertEqual(self.cipher.combine_character("D", "E"), "H")

    def test_combine_non_alpha(self):
        self.assertRaises(ValueError, self.cipher.combine_character, "@", "t")
        # The name of the function or method is required (without calling the function), followed by
        # *args and **kwargs

    def test_combine_character_mod(self):
        self.assertEqual(self.cipher.combine_character("W", "F"), "B")

    def test_combine_lower(self):
        self.assertEqual(self.cipher.combine_character("y", "t"), "R")



    def test_encode(self):
        encoded_text = self.cipher.encode("ENCODEINPYTHON")
        self.assertEqual(encoded_text, 'XECWQXUIVCRKHWA')


if __name__ == '__main__':
    unittest.main()
