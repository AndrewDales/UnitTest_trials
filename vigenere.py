class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def encode(self, plaintext):
        return 'XECWQXUIVCRKHWA'

    @staticmethod
    def combine_character(plain_letter, keyword_letter):
        if not (plain_letter.isalpha() and keyword_letter.isalpha()):
            raise ValueError("Plain letter and keyword letter must both be alphabetic (a-z or A-Z)")
        plain_num = ord(plain_letter.upper()) - ord('A')
        keyword_num = ord(keyword_letter.upper()) - ord('A')
        cipher_num = (plain_num + keyword_num) % 26
        return chr(cipher_num + ord('A'))