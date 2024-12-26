# pip install pycryptodome
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# 1. 비밀번호 해싱 및 검증
def hash_password(password):
    """비밀번호를 SHA-256으로 해싱합니다."""
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()

def verify_password(stored_hash, input_password):
    """저장된 해시와 입력된 비밀번호의 해시를 비교합니다."""
    return stored_hash == hash_password(input_password)


# 2. 데이터 무결성 확인
def hash_file(file_path):
    """파일의 SHA-256 해시를 계산합니다."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()


# 3. 디지털 서명 생성 및 검증
def create_signature(message, private_key):
    """SHA-256 해시를 기반으로 디지털 서명을 생성합니다."""
    h = SHA256.new(message.encode())
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

def verify_signature(message, signature, public_key):
    """디지털 서명이 유효한지 검증합니다."""
    h = SHA256.new(message.encode())
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False


# 메인 함수
def main():
    # 1. 비밀번호 해싱 및 검증
    print("\n[비밀번호 해싱 및 검증]")
    password = "securepassword123"
    stored_hash = hash_password(password)
    print("저장된 비밀번호 해시:", stored_hash)

    input_password = "securepassword123"
    is_valid_password = verify_password(stored_hash, input_password)
    print(f"비밀번호 검증 결과 ({input_password}):", is_valid_password)

    # 2. 데이터 무결성 확인
    print("\n[데이터 무결성 확인]")
    with open("example.txt", "w") as f:
        f.write("This is an example file.")

    original_hash = hash_file("example.txt")
    print("원본 파일 해시:", original_hash)

    # 파일이 수정되었는지 확인
    modified_hash = hash_file("example.txt")
    print("수정된 파일 해시:", modified_hash)

    is_intact = original_hash == modified_hash
    print("파일 무결성 검증 성공 여부:", is_intact)

    # 3. 디지털 서명 생성 및 검증
    print("\n[디지털 서명 시뮬레이션]")
    # RSA 키 생성
    key = RSA.generate(2048)
    private_key = key
    public_key = key.public_key()

    # 메시지 서명
    message = "This is a secure message."
    signature = create_signature(message, private_key)
    print("서명 생성 완료")

    # 서명 검증
    is_valid_signature = verify_signature(message, signature, public_key)
    print("서명 검증 성공 여부:", is_valid_signature)


# 실행
if __name__ == "__main__":
    main()
