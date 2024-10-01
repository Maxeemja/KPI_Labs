def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, key):
    return encrypt(text, -key)

# Приклад використання:
plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
key = 3
encrypted_text = encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
