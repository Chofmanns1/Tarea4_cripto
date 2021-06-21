from Crypto import Cipher
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode
import os

hashes = []
encrypt_arr = []
decrypt_arr = []


key = RSA.generate(2048)

def encrypt(clear_msg, public_k):
    cipher = PKCS1_OAEP.new(public_k)
    return b64encode(cipher.encrypt(clear_msg))

def decrypt(secret_msg, key):
    decryptor = PKCS1_OAEP.new(key)
    return decryptor.decrypt(b64decode(secret_msg))

os.chdir("C:/Users/crist/Desktop/Cripto/Tarea4/hashcat-6.2.2")

with open('hashed_file.txt', 'r') as f:
    first_line = f.readline()
    hashes.append(first_line.encode())
    for i in f:
        hashes.append(i.encode())

for i in hashes:
    encrypted_msg = encrypt(i, key.publickey())
    encrypt_arr.append(encrypted_msg)

print("\nArreglo 1: \n")
for i in hashes:
    print(i)

print("\nMensajes encriptados: \n")
for i in encrypt_arr:
    print(i)

for i in encrypt_arr:
    decrypted_msg = decrypt(i, key)
    decrypt_arr.append(decrypted_msg)

print("\nMensajes desencriptados: \n")
for i in decrypt_arr:
    print(i)


#decrypted_msg = decrypt(encrypted_msg, key)

#print("Mensaje desencriptado:")
#print(decrypted_msg)