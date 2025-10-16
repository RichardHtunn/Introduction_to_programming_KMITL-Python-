cipher_key = {
    ('A', 'A'): 'b', ('A', 'D'): 't', ('A', 'F'): 'a', ('A', 'G'): 'l', ('A', 'X'): 'p',
    ('D', 'A'): 'd', ('D', 'D'): 'h', ('D', 'F'): 'o', ('D', 'G'): 'z', ('D', 'X'): 'k',
    ('F', 'A'): 'q', ('F', 'D'): 'f', ('F', 'F'): 'v', ('F', 'G'): 's', ('F', 'X'): 'n',
    ('G', 'A'): 'g', ('G', 'D'): 'i/j', ('G', 'F'): 'c', ('G', 'G'): 'u', ('G', 'X'): 'x',
    ('X', 'A'): 'm', ('X', 'D'): 'r', ('X', 'F'): 'e', ('X', 'G'): 'w', ('X', 'X'): 'y'
}

def decrypt_key(cipherkey):
    if len(cipherkey) % 2 != 0 or any(c not in "ADFGX" for c in cipherkey): # check whether ADFGX is in "cipherkey"
        return "FAILED TO DECRYPT"

    decrypted_message = ""
    for i in range(0, len(cipherkey),2): # user increasement 2 becasue the pair gonna be 2 letters
        pair = (cipherkey[i], cipherkey[i+1]) # pair gonna be tuple because the keys in the cipher_key dict are the tuples

        if pair in cipher_key:
            decrypted_message += cipher_key[pair]
        else:
            return "FAILED TO DECRYPT"
    
    return decrypted_message

cipherkey = input("Input ADFGX cipher text : ").strip().upper()
decrypted_message = decrypt_key(cipherkey)
print(decrypted_message)