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
        self.assertRaises(TypeError, VigenereCipher, 20)

    def test_combine_character(self):
        self.assertEqual(self.cipher._combine_character("D", "E"), "H")

    def test_combine_non_alpha(self):
        self.assertRaises(ValueError, self.cipher._combine_character, "@", "t")

    def test_combine_character_mod(self):
        self.assertEqual(self.cipher._combine_character("W", "F"), "B")

    def test_combine_lower(self):
        self.assertEqual(self.cipher._combine_character("y", "t"), "R")

    def test_separate_character(self):
        self.assertEqual(self.cipher._separate_character("W", "I"), "O")
        self.assertEqual(self.cipher._separate_character("p", "e"), "L")

    def test_extend_keyword(self):
        self.assertEqual(self.cipher._extend_keyword(12), "TRAINTRAINTR")
        cipher = VigenereCipher("CHEESE")
        self.assertEqual(cipher._extend_keyword(18), "CHEESECHEESECHEESE")

    def test_encode(self):
        self.assertEqual(self.cipher.encode("ENCODEDINPYTHON"), "XECWQXUIVCRKHWA")
        self.assertEqual(self.cipher.encode("Give me cheese please"), "ZZVMZXTHMRLVPTRTJE")
        cipher = VigenereCipher("computer")
        self.assertEqual(cipher.encode("Meet me at the bridge at dawn"), "OSQIGXEKVVQQLBHXGOFSUPR")

    def test_encode_validate(self):
        self.assertRaises(ValueError, self.cipher.encode, "$%FG")
        self.assertRaises(TypeError, self.cipher.encode, (5, 6))

    def test_decode(self):
        self.assertEqual(self.cipher.decode("XECWQXUIVCRKHWA"), "ENCODEDINPYTHON")
        cipher = VigenereCipher("trunk")
        self.assertEqual(cipher.decode("MFGBBKFQAOOVLQSXJ"), "TOMORROWNEVERDIES")


if __name__ == '__main__':
    unittest.main()
