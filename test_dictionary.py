import unittest
from unittest import TestCase
from dictionary import EnglishDict


class TestEnglishDict(TestCase):
    def setUp(self):
        self.dictionary = EnglishDict()

    def test_init(self):
        self.assertIn("initial", self.dictionary.words)
        self.assertNotIn("oiasdf", self.dictionary.words)
        self.assertNotIn("GoodBye", self.dictionary.words)

    def test_check_word(self):
        self.assertTrue(self.dictionary.check_word("hello"))
        self.assertTrue(self.dictionary.check_word("GoodBye"))
        self.assertFalse(self.dictionary.check_word("sakdjfasdfj"))
        self.assertRaises(TypeError, self.dictionary.check_word, 5)

    def test_starts_with(self):
        self.assertIn("speaker", self.dictionary.starts_with("sp"))
        self.assertNotIn("sting", self.dictionary.starts_with("su"))
        self.assertNotIn("speaker", self.dictionary.starts_with("sp", 8))


if __name__ == '__main__':
    unittest.main()

