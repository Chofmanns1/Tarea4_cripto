import bcrypt
import os

os.chdir("C:/Users/crist/Desktop/Cripto/Tarea4/hashcat-6.2.2")

passwords = []
passh = []

# Pasar de archivos de texto a arreglos

with open('simple_output_arch1.txt', 'r') as f:
    first_line = f.readline()
    passwords.append(first_line.encode())
    for i in f:
        passwords.append(i.encode())

with open('simple_output_arch2.txt', 'r') as f:
    first_line = f.readline()
    passwords.append(first_line.encode())
    for i in f:
        passwords.append(i.encode())

with open('simple_output_arch3.txt', 'r') as f:
    first_line = f.readline()
    passwords.append(first_line.encode())
    for i in f:
        passwords.append(i.encode())

with open('simple_output_arch4.txt', 'r') as f:
    first_line = f.readline()
    passwords.append(first_line.encode())
    for i in f:
        passwords.append(i.encode())

with open('simple_output_arch5.txt', 'r') as f:
    first_line = f.readline()
    passwords.append(first_line.encode())
    for i in f:
        passwords.append(i.encode())

#o = open('todo.txt', 'w')

#for i in passwords:
    #o.write(i.decode())

# Hashear

for i in passwords:
    hashed = bcrypt.hashpw(i, bcrypt.gensalt())
    passh.append(hashed)

hashed_file = open('hashed_file.txt', 'w')
for i in passh:
    hashed_file.write(i.decode()+'\n')


#print(passwords)
#print(passh)

