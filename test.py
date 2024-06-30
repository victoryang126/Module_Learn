from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# 生成ECC密钥对
private_key = ec.generate_private_key(ec.SECP384R1())
public_key = private_key.public_key()

# 导出并显示公钥
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(f"公钥: {public_key_bytes.decode('utf-8')}")

# 待签名的消息
message = b"这是一个需要签名的消息"

# 签名
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)
print(f"签名: {signature}")

# 验证签名
try:
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    print("签名验证成功!")
except Exception as e:
    print(f"签名验证失败: {e}")
