from Crypto.Cipher import DES
form Crypto.Hash import SHA256 as SHA

class myDES():
    def __init__(self,keytext,ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key= hash.digest()
        self.key=key[:8]

        hash.update(ivtext.encode('utf-8'))
        iv=hash.digest()
        self.iv=iv[:8]

    def encrypt_ECB(self,plaintext):
        while(len(plaintext)%8!=0):
            plaintext+=' '
        des=DES.new(self,key,DES.MODE_ECB)
        encryptMsg =des.encrypt(plaintext.encode())
        return encryptMsg
    def decrypt_ECB(self,ciphertext):
        des = DES.new(self.key,DES.MODE_ECB)
        decryptMsg = des.decrypt(ciphertext)
        return decryptMsg
    
    def encrpt_CBC(self,plaintext):
        while(len(plaintext)%8!=0):
            plaintext+=' '
        des=DES.new(self,key,DES,MODE_CBC,self.iv)
        encryptMsg =des.encrypt(plaintext.encode())
        return encryptMsg
    def decrpt_CBC(self,ciphertext):
        des=DES.new(self.key, DES.MODE_CBC,self.iv)
        descryptMsg= des.decrypt(ciphertext)
        return descryptMsg
