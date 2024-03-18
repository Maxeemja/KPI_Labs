import random
import time

import docx
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad, pad


def read_text_from_doc():
    doc = docx.Document("text.docx")
    plain_text = ""
    for paragraph in doc.paragraphs:
        plain_text += paragraph.text

    return plain_text


def generate_key():
    key = bytes([random.randint(0, 255) for _ in range(8)])
    return key


def encrypt(text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text.encode('utf-8'), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text


def decrypt(cipher, key):
    cipher_obj = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher_obj.decrypt(cipher)
    unpadded_text = unpad(decrypted_text, DES.block_size)
    return unpadded_text.decode('utf-8')


message = read_text_from_doc()
print("Length of input message:", len(message))

encrypting_key = generate_key()
print("Generated key:", encrypting_key)

start = time.time()
encoded_text = encrypt(message, encrypting_key)
print("Encoding time:", time.time() - start)

start = time.time()
decoded_text = decrypt(encoded_text, encrypting_key)
print("Decoding time:", time.time() - start)
print("Decoded:", decoded_text)
