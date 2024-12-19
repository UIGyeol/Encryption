# -*- coding: utf-8 -*-
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

"""No module named 'Crypto'오류시
pip install pycrptodome실행
"""

pip install pycryptodome

"""오류 났던 부분 다시 실행
-from Crypto.PublicKey import RSA

-from Crypto.Cipher import PKCS1_OAEP
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

"""키 생성및 저장 함수

함수 make_key 정의

1.   2048길이의 키 생성
2.   생성된 프라이빗키로 퍼블릭키 생성
3.   프라이빗 키를 파일로 저장
4.   퍼블릭 키를 파일로 저장
"""

def make_key():
  pr_key=RSA.generate(2048)
  print(pr_key)
  pu_key=pr_key.public_key()
  print(pu_key)
  return pr_key, pu_key

  pr_file=open("pr.key","wb")
  pr_file.write(pr_key.export_key('PEM'))
  pr_file.close()

  pu_file=open("pu.key",'wb')
  pu_file.write(pu_key.export_key('PEM'))
  pu_file.close()

"""함수 실행"""

make_key()
