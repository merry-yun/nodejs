from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex
import base64

# Determine salt and ciphertext
# encryptedDataB64 = 'U2FsdGVkX18cqUNRkszsHA4Oo7U0ciqrx8EyxOMo7AP/8TI6M+nS8D+kECY4TQTpioTK2rXK/TUO10W7Tytrsw=='
encryptedDataB64 = 'U2FsdGVkX197SM3Eh62XyjAwTXznW9DdALdNR1gKNsewAg3fzwA0x/+UQldlbi3oYBn8eFHgTtBUcGneYPCjIA=='
print(len(encryptedDataB64))
encryptedData = base64.b64decode(encryptedDataB64)
print(encryptedData)
salt = encryptedData[8:16]

ciphertext = encryptedData[16:]
print(salt)
print(ciphertext)
# Reconstruct Key/IV-pair
pbkdf2Hash = PBKDF2(b'"mypassword"', salt, 32 + 16, count=100000, hmac_hash_module=SHA256)
print(len(pbkdf2Hash))
key = pbkdf2Hash[0:32]
print(b2a_hex(key))
iv = pbkdf2Hash[32:32 + 16]
print(key, iv)
print(AES.block_size)

# Decrypt with AES-256 / CBC / PKCS7 Padding
cipher = AES.new(key, AES.MODE_CBC, iv)
result = b2a_hex(cipher.decrypt(ciphertext))
word = base64.b64encode(result)
print(word)
# decrypted = unpad(cipher.decrypt(ciphertext), 16)

# print(decrypted)