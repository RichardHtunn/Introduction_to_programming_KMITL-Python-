cipher_key = {
    ('A', 'A'): 'b', ('A', 'D'): 't', ('A', 'F'): 'a', ('A', 'G'): 'l', ('A', 'X'): 'p',
    ('D', 'A'): 'd', ('D', 'D'): 'h', ('D', 'F'): 'o', ('D', 'G'): 'z', ('D', 'X'): 'k',
    ('F', 'A'): 'q', ('F', 'D'): 'f', ('F', 'F'): 'v', ('F', 'G'): 's', ('F', 'X'): 'n',
    ('G', 'A'): 'g', ('G', 'D'): 'i/j', ('G', 'F'): 'c', ('G', 'G'): 'u', ('G', 'X'): 'x',
    ('X', 'A'): 'm', ('X', 'D'): 'r', ('X', 'F'): 'e', ('X', 'G'): 'w', ('X', 'X'): 'y'
}

def decrypt(ciphertext):
    if len(ciphertext) % 2 != 0 or any(c not in "ADFGX" for c in ciphertext):
        return "FAILED TO DECRYPT"
    
    decrypted_message = ""
    for i in range(0, len(ciphertext), 2):
        pair = (ciphertext[i], ciphertext[i+1])
        if pair in cipher_key:
            decrypted_message += cipher_key[pair]
        else:
            return "FAILED TO DECRYPT"
    return decrypted_message

ciphertext = input("Input ADFGX : ").strip().upper()
decrypted_message = decrypt(ciphertext)
print(decrypted_message)