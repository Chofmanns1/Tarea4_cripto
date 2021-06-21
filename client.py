import socket
import os
import subprocess
import bcrypt

passwords1 = []
passwords2 = []
passwords3 = []
passwords4 = []
passwords5 = []
passh1 = []
passh2 = []
passh3 = []
passh4 = []
passh5 = []

os.chdir("C:/Users/crist/Desktop/Cripto/Tarea4/hashcat-6.2.2")
subprocess.run("hashcat.exe -m 0 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_1 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force", shell=True)
subprocess.run("hashcat.exe -m 0 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_1 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force --show --outfile=simple_output_arch1.txt --outfile-format=2", shell=True)
subprocess.run("hashcat.exe -m 10 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_2 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force", shell=True)
subprocess.run("hashcat.exe -m 10 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_2 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force --show --outfile=simple_output_arch2.txt --outfile-format=2", shell=True)
subprocess.run("hashcat.exe -m 10 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_3 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force", shell=True)
subprocess.run("hashcat.exe -m 10 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_3 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force --show --outfile=simple_output_arch3.txt --outfile-format=2", shell=True)
subprocess.run("hashcat.exe -m 1000 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_4 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force", shell=True)
subprocess.run("hashcat.exe -m 1000 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_4 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force --show --outfile=simple_output_arch4.txt --outfile-format=2", shell=True)
subprocess.run("hashcat.exe -m 1800 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_5 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force", shell=True)
subprocess.run("hashcat.exe -m 1800 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_5 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force --show --outfile=simple_output_arch5.txt --outfile-format=2", shell=True)

# Pasar de archivos de texto a arreglos

with open('simple_output_arch1.txt', 'r') as f:
    f.readline()
    for i in f:
        passwords1.append(i.encode())

with open('simple_output_arch2.txt', 'r') as f:
    f.readline()
    for i in f:
        passwords2.append(i.encode())

with open('simple_output_arch3.txt', 'r') as f:
    f.readline()
    for i in f:
        passwords3.append(i.encode())

with open('simple_output_arch4.txt', 'r') as f:
    f.readline()
    for i in f:
        passwords4.append(i.encode())

with open('simple_output_arch5.txt', 'r') as f:
    f.readline()
    for i in f:
        passwords5.append(i.encode())

# Hashear cada uno de los arreglos

for i in passwords1:
    hashed = bcrypt.hashpw(i, bcrypt.gensalt())
    passh1.append(hashed)

for i in passwords2:
    hashed = bcrypt.hashpw(i, bcrypt.gensalt())
    passh2.append(hashed)

for i in passwords3:
    hashed = bcrypt.hashpw(i, bcrypt.gensalt())
    passh3.append(hashed)

for i in passwords4:
    hashed = bcrypt.hashpw(i, bcrypt.gensalt())
    passh4.append(hashed)

for i in passwords5:
    hashed = bcrypt.hashpw(i, bcrypt.gensalt())
    passh5.append(hashed)

hashed_file1 = open('hashed_file1.txt', 'w')
for i in passh1:
    hashed_file1.write(i+'\n')

hashed_file2 = open('hashed_file2.txt', 'w')
for i in passh2:
    hashed_file2.write(i+'\n')

hashed_file3 = open('hashed_file3.txt', 'w')
for i in passh3:
    hashed_file3.write(i+'\n')

hashed_file4 = open('hashed_file4.txt', 'w')
for i in passh4:
    hashed_file4.write(i+'\n')

hashed_file5 = open('hashed_file5.txt', 'w')
for i in passh5:
    hashed_file5.write(i+'\n')

hashed_file1.close()
hashed_file2.close()
hashed_file3.close()
hashed_file4.close()
hashed_file5.close()

mi_socket = socket.socket()
mi_socket.connect(('localhost', 8000))
a1 = "hashed_file1.txt"
a2 = "hashed_file2.txt"
a3 = "hashed_file3.txt"
a4 = "hashed_file4.txt"
a5 = "hashed_file5.txt"

#mi_socket.send(b"Hola desde el cliente")
respuesta = mi_socket.recv(1024)

print(respuesta)
mi_socket.close()