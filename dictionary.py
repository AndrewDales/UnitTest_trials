class EnglishDict:
    def __init__(self, words=None):
        if not words:
            with open('english3_justwords.txt') as word_file:
                words = set(word_file.read().split())
        self.words = words

    def check_word(self, word):
        if isinstance(word, str):
            return word.lower() in self.words and len(word) >= 3
        else:
            raise TypeError("Input must be a string")

    def starts_with(self, start_word: str, min_len=1):
        start_word = start_word.lower()
        return set(word for word in self.words if word.startswith(start_word) and len(word) >= min_len)
