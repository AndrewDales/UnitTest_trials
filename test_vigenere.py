import unittest
from vigenere import VigenereCipher


class VigenereTestCase(unittest.TestCase):
    def setUp(self):
        self.cipher = VigenereCipher("TRAIN")

    def test_init(self):
        self.assertEqual(self.cipher.keyword, "TRAIN")

    def test_init_lower(self):
        cipher = VigenereCipher("taxi")
        self.assertEqual(cipher.keyword, "TAXI")

    def test_init_invalid(self):
        self.assertRaises(ValueError, VigenereCipher, "$%FG")

    def test_combine_characer(self):
        self.assertEqual(self.cipher._combine_character("D", "E"), "H")

    def test_combine_non_alpha(self):
        self.assertRaises(ValueError, self.cipher._combine_character, "@", "t")
        # The name of the function or method is required (without calling the function), followed by
        # *args and **kwargs

    def test_combine_character_mod(self):
        self.assertEqual(self.cipher._combine_character("W", "F"), "B")

    def test_combine_lower(self):
        self.assertEqual(self.cipher._combine_character("y", "t"), "R")

    def test_encode(self):
        encoded_text = self.cipher.encode("ENCODEINPYTHON")
        self.assertEqual(encoded_text, 'XECWQXUIVCRKHWA')

    def test_extend_keyword(self):
        self.assertEqual(self.cipher.extend_keyword(12), "TRAINTRAINTR")
        cipher = VigenereCipher("CHEESE")
        self.assertEqual(cipher.extend_keyword(18), "CHEESECHEESECHEESE")

if __name__ == '__main__':
    unittest.main()
