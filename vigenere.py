# Membuat key yang berulang yang sama panjang 
# dengan plaintext/ciphertext
def generateKey(String, key):
    key = list(key)

    if(len(String) == len(key)):
        return(key)
    else:
        for i in range(len(String) - len(key)):
            key.append(key[i % len(key)])
        return "".join(key)
# P = ascii code plaintext K = ascii code ciphertext
# Mengenkripsi plaintext menjadi ciphertext
# (P + K) % 26 
def encrypt(string, key):
    kunci = generateKey(string, key)
    cipherText = ""
    for i in range(len(string)):
        cipherText += chr(((ord(string[i]) + ord(kunci[i])) % 26) + 65)
    return cipherText

# Mendeskripsi ciphertext
# (P - K + 26) % 26
def decrypt(string, key):
    kunci = generateKey(string, key)
    plainText = ""
    
    for i in range(len(string)):
        if(ord(string[i])>64 and ord(string[i])<91):
            plainText += chr(((ord(string[i]) - ord(kunci[i]) + 26) % 26) + 65)
        elif(ord(string[i])>96 and ord(string[i])<123):
            plainText += chr(((ord(string[i]) - ord(kunci[i]) + 26) % 26) + 97)
        else:
            plainText += string[i]
    return plainText

print("=============Vigenere Cipher=============")
string = input("Masukkan text : ")
keyword = input("Masukkan key : ")
chs = input("encrypt/decrypt (e/d)? ")
if(chs == "e"):
    print(encrypt(string, keyword))
else:
    print(decrypt(string, keyword))