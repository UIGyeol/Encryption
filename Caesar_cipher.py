class CaesarCipher:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.cryption_txt = []
        self.decryption_txt = []
        
    def set_cryption(self):
        for char in self.plain_text:
            self.cryption_txt.append(chr(ord(char) + 3))
    
    def get_cryption(self):
        print(f"Encrypted text: {self.cryption_txt}")

    def set_decryption(self):
        for char in self.cryption_txt:
            self.decryption_txt.append(chr(ord(char) - 3))
    
    def get_decryption(self):
        print(f"Decrypted text:{self.decryption_txt}")


plain_text = input("Please input your message: ")
test1 = CaesarCipher(plain_text)
test1.set_cryption()
test1.get_cryption()
test1.set_decryption()
test1.get_decryption()
