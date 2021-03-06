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

    def _extend_keyword(self, msg_length):
        d, m = divmod(msg_length, len(self.keyword))
        return self.keyword * d + self.keyword[:m]

    # def encode(self, plaintext):
    #     if not isinstance(plaintext, str):
    #         raise TypeError("Plaintext must be a string")
    #     plaintext_msg = plaintext.replace(" ", "")
    #     if not plaintext_msg.isalpha():
    #         raise ValueError("Plaintext must include only alphabetic characters (a-z or A-Z")
    #     cipher_letters = [self._combine_character(p, k)
    #                       for p, k in zip(plaintext_msg, self._extend_keyword(len(plaintext_msg)))]
    #     return "".join(cipher_letters)
    #
    # def decode(self, ciphertext):
    #     if not isinstance(ciphertext, str):
    #         raise TypeError("Ciphertext must be a string")
    #     ciphertext_msg = ciphertext.replace(" ", "")
    #     if not ciphertext_msg.isalpha():
    #         raise ValueError("Ciphertext must include only alphabetic characters (a-z or A-Z")
    #     cipher_letters = [self._separate_character(p, k)
    #                       for p, k in zip(ciphertext_msg, self._extend_keyword(len(ciphertext_msg)))]
    #     return "".join(cipher_letters)

    # The following shows refactored code that improves the encode and decode methods
    # by removing repeated elements

    def _code(self, text, combine_function):
        if not isinstance(text, str):
            raise TypeError("Entered text must be a string")
        text = text.replace(" ", "")
        if not text.isalpha():
            raise ValueError("Entered text must include only alphabetic characters (a-z or A-Z")
        extended_keyword = self._extend_keyword(len(text))
        coded_letters = [combine_function(p, k)
                         for p, k in zip(text, extended_keyword)]
        return "".join(coded_letters)

    def encode(self, plaintext):
        return self._code(plaintext, self._combine_character)

    def decode(self, cipher_text):
        return self._code(cipher_text, self._separate_character)
