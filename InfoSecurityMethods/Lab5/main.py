import time
import random
import math

alphabet = "abcdefghijklmnopqrstuvwxyz"


def read_text_from_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return file.read().strip()


original_text = read_text_from_file("text.txt")


def key_generation():
    while True:
        key_a = random.randint(2, len(alphabet))
        if math.gcd(key_a, len(alphabet)) == 1:
            break
    key_b = random.randint(2, len(alphabet))
    key_c = random.randint(2, len(alphabet))
    return key_a, key_b, key_c


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def encode(text, key_a, key_b, key_c):
    start_time = time.time()
    encoded_text = ""
    for symbol in range(len(text)):
        if text[symbol] in alphabet:
            encoded_text += alphabet[((alphabet.index(text[symbol]) * key_a + key_b) % len(alphabet))]
        else:
            encoded_text += text[symbol]
    encrypted = ""
    for symbol in range(len(encoded_text)):
        if encoded_text[symbol] in alphabet:
            encrypted += alphabet[((alphabet.index(encoded_text[symbol]) * key_a + key_b + key_c) % len(alphabet))]
        else:
            encrypted += encoded_text[symbol]
    operation_time = time.time() - start_time
    return encrypted, operation_time


def decode(text, a_inverse, key_b, key_c):
    start_time = time.time()
    decoded_text = ""
    for symbol in range(len(text)):
        if text[symbol] in alphabet:
            decoded_text += alphabet[((a_inverse * (alphabet.index(text[symbol]) - key_b)) % len(alphabet))]
        else:
            decoded_text += text[symbol]
    decrypted = ""
    for symbol in range(len(decoded_text)):
        if decoded_text[symbol] in alphabet:
            decrypted += alphabet[(((alphabet.index(decoded_text[symbol]) - key_b) * a_inverse - key_c) % len(alphabet))]
        else:
            decrypted += decoded_text[symbol]
    operation_time = time.time() - start_time
    return decrypted, operation_time


def brute_force(encoded_text, original_text):
    start_time = time.time()
    processing_text = ""
    counter = 1
    key_list = [0] * 3

    while original_text != processing_text:
        key_list[len(key_list) - 1] += 1
        for i in range(len(key_list)):
            if key_list[(len(key_list) - (i + 1))] == len(alphabet):
                key_list[(len(key_list) - (i + 1))] = 0
                key_list[len(key_list) - (i + 2)] += 1

        processing_text, _ = decode(encoded_text, key_list[0], key_list[1], key_list[2])
        counter += 1

    operation_time = time.time() - start_time
    return processing_text, counter, operation_time


a, b, c = key_generation()
a_1 = mod_inverse(a, len(alphabet))
encoded, encoding_time = encode(original_text, a, b, c)
decoded, decoding_time = decode(encoded, a_1, b, c)
hacked_text, iterations, hacking_time = brute_force(encoded, original_text)

print("Encoding keys:", a, b, c)
print("Encoded text:", encoded)
print("Decoded text:", decoded, "\n")
print(f"Hacked text is: {hacked_text} \nIt took {hacking_time}s and {iterations} iterations.")
