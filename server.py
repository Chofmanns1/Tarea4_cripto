import socket
from Crypto import Cipher
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode

key = RSA.generate(2048)

def encrypt(clear_msg, public_k):
    cipher = PKCS1_OAEP.new(public_k)
    return b64encode(cipher.encrypt(clear_msg))

def decrypt(secret_msg, key):
    decryptor = PKCS1_OAEP.new(key)
    return decryptor.decrypt(b64decode(secret_msg))

mi_socket = socket.socket()
mi_socket.bind(('localhost', 8000))
mi_socket.listen(5)

while True:
    conexion, addr = mi_socket.accept()
    #print(b"LASJDAKLSJDLKADJS")
    print(addr)

    peticion = conexion.recv(1024)
    print(peticion)

    conexion.send(b"HOASLDASDLKJASD")
    conexion.close()