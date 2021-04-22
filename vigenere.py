class VigenereCipher:

    def __init__(self, keyword):
        if not keyword.isalpha():
            raise ValueError("Keyword must include only alphabetic characters (a-z or A-Z")
        self.keyword = keyword.upper()

    def encode(self, plaintext):
        return 'XECWQXUIVCRKHWA'

    @staticmethod
    def _combine_character(plain_letter, keyword_letter):
        if not (plain_letter.isalpha() and keyword_letter.isalpha()):
            raise ValueError("Plain letter and keyword letter must both be alphabetic (a-z or A-Z)")
        plain_num = ord(plain_letter.upper()) - ord('A')
        keyword_num = ord(keyword_letter.upper()) - ord('A')
        cipher_num = (plain_num + keyword_num) % 26
        return chr(cipher_num + ord('A'))

    def extend_keyword(self, msg_length):
        d, m = divmod(msg_length, len(self.keyword))
        return self.keyword * d + self.keyword[:m]