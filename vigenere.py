class VigenereCipher:

    # TODO consolidate validation code into a private method
    def __init__(self, keyword):
        if not isinstance(keyword, str):
            raise TypeError("Keyword must be a string")
        if not keyword.isalpha():
            raise ValueError("Keyword must include only alphabetic characters (a-z or A-Z")
        self.keyword = keyword.upper()

    @staticmethod
    def _combine_character(plain_letter, keyword_letter):
        if not (plain_letter.isalpha() and keyword_letter.isalpha()):
            raise ValueError("Plain letter and keyword letter must both be alphabetic (a-z or A-Z)")
        plain_num = ord(plain_letter.upper()) - ord('A')
        keyword_num = ord(keyword_letter.upper()) - ord('A')
        cipher_num = (plain_num + keyword_num) % 26
        return chr(cipher_num + ord('A'))

    @staticmethod
    def _separate_character(cipher_letter, keyword_letter):
        cipher_num = ord(cipher_letter.upper()) - ord('A')
        keyword_num = ord(keyword_letter.upper()) - ord('A')
        plain_num = (cipher_num - keyword_num) % 26
        return chr(plain_num + ord('A'))

    def extend_keyword(self, msg_length):
        d, m = divmod(msg_length, len(self.keyword))
        return self.keyword * d + self.keyword[:m]

    def _code(self, text, combine_func):
        if not isinstance(text, str):
            raise TypeError("Plaintext must be a string")
        text = text.replace(" ", "")
        if not text.isalpha():
            raise ValueError("Plaintext must include only alphabetic characters (a-z or A-Z)")
        combined = [combine_func(p, k)
                    for p, k in zip(text, self.extend_keyword(len(text)))]
        return "".join(combined)

    def encode(self, plaintext):
        return self._code(plaintext, combine_func=self._combine_character)

    def decode(self, ciphertext):
        return self._code(ciphertext, combine_func=self._separate_character)
