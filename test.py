from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.hkdf import HKDFExpand
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.concatkdf import ConcatKDFHash
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# 生成ECC密钥对
private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
public_key = private_key.public_key()

# 导出并显示公钥
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(f"公钥: {public_key_bytes.decode('utf-8')}")

# 待加密的消息
message = b"这是一个秘密消息"

# 加密
# 使用对方的公钥生成共享密钥
peer_public_key = public_key
shared_key = private_key.exchange(ec.ECDH(), peer_public_key)

# 派生一个对称密钥
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
    backend=default_backend()
).derive(shared_key)

# 使用对称密钥进行加密
iv = b'\x00' * 16  # 初始化向量
cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()

# 使用PKCS7填充
padder = sym_padding.PKCS7(algorithms.AES.block_size).padder()
padded_data = padder.update(message) + padder.finalize()

encrypted_message = encryptor.update(padded_data) + encryptor.finalize()
print(f"加密后的消息: {encrypted_message}")

# 解密
# 使用对方的公钥生成共享密钥
shared_key = private_key.exchange(ec.ECDH(), peer_public_key)

# 派生一个对称密钥
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
    backend=default_backend()
).derive(shared_key)

# 使用对称密钥进行解密
cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()

decrypted_padded_message = decryptor.update(encrypted_message) + decryptor.finalize()

# 去除填充
unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
decrypted_message = unpadder.update(decrypted_padded_message) + unpadder.finalize()

print(f"解密后的消息: {decrypted_message.decode('utf-8')}")
