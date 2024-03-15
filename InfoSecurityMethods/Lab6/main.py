import random
import time
import docx


def KSA(key):
    key_length = len(key)
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % key_length]) % 256
        s[i], s[j] = s[j], s[i]
    return s


def PRGA(s):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        yield k


def get_key_stream(key):
    s = KSA(key)
    return PRGA(s)


def encrypt(message, key):
    key = key.encode("utf-8")
    key_stream = get_key_stream(key)
    message = message.encode("utf-8")
    cipher = bytearray()
    for byte in message:
        cipher.append(byte ^ next(key_stream))
    return cipher.hex()


def decrypt(cipher, key):
    key = key.encode("utf-8")
    key_stream = get_key_stream(key)
    cipher = bytes.fromhex(cipher)
    message = bytearray()
    for byte in cipher:
        message.append(byte ^ next(key_stream))
    return message.decode("utf-8")


def brute_force(encoded_text, original_text):
    processing_text = ""
    counter = 0
    key_list = ['a']

    while original_text != processing_text:
        try:
            processing_text = decrypt(encoded_text, *key_list)
        except UnicodeDecodeError:
            pass
        counter += 1
        update_key(key_list)

    return processing_text, counter


def update_key(key):
    if key[0] == 'z':
        key[0] = 'a'
    else:
        key[0] = chr(ord(key[0]) + 1)


def read_text_from_txt():
    with open("text.txt", 'r', encoding="utf-8") as file:
        return file.read().strip()


def read_text_from_doc():
    doc = docx.Document("text.docx")
    plain_text = ""
    for paragraph in doc.paragraphs:
        plain_text += paragraph.text

    return plain_text


plaintext = read_text_from_doc()

key_alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = "".join(random.choice(key_alphabet) for _ in range(1))

print("Original text:", plaintext)
print("Generated key:", key)
print("-" * 20)

# Encryption
startTime = time.time()
encrypted = encrypt(plaintext, key)
print("Encrypted text:", encrypted)
print("Encrypting time:", time.time() - startTime)
print("-" * 20)

# Decryption
startTime = time.time()
decrypted = decrypt(encrypted, key)
print("Decrypted text:", decrypted)
print("Decrypting time:", time.time() - startTime)
print("-" * 20)

# Brute Force Attack
startTime = time.time()
hacked_text, iterations = brute_force(encrypted, plaintext)
print("Hacked text:", hacked_text)
print("Iterations:", iterations)
print("Hacking time:", time.time() - startTime)
print("-" * 20)
