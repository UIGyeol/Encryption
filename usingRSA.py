import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def make_key():
    pr_key = RSA.generate(2048)
    pu_key = pr_key.public_key()

    with open("pr.key", "wb") as pr_file:
        pr_file.write(pr_key.export_key('PEM'))


    with open("pu.key", "wb") as pu_file:
        pu_file.write(pu_key.export_key('PEM'))

    return pr_key, pu_key

def encrypt(msg, pu_key):
    cipher = PKCS1_OAEP.new(pu_key)
    msg_enc = cipher.encrypt(msg)
    return msg_enc

def decrypt(msg_enc, pr_key):
    cipher = PKCS1_OAEP.new(pr_key)
    msg = cipher.decrypt(msg_enc)
    return msg

def get_key(path):
    with open(path, 'rb') as fr:
        key = RSA.import_key(fr.read())
    return key

def main():
    msg = 'this is crypto'

    # 키 가져오기
    pu_key = get_key('pu.key')
    pr_key = get_key('pr.key')

    # 메시지 암호화
    msg_enc = encrypt(msg.encode(), pu_key)

    # 암호화된 메시지 출력 (Base64 인코딩)
    print("원래의 내용: ", msg)
    print("암호화된 내용: ", base64.b64encode(msg_enc).decode())

    # 메시지 복호화
    msg_dec = decrypt(msg_enc, pr_key)
    print("복호화된 내용: ", msg_dec.decode())

# 키를 먼저 생성 (한 번만 실행)
# make_key()

# 메인 함수 실행
def main():
  msg='this is crypto'
  pu_key=get_key('pu.key')
  msg_enc=encrypt_msg(msg.encode(),pu_key)
  
  print("원래의 내용: ",msg)
  print("암호화된 내용: ", msg_enc)
