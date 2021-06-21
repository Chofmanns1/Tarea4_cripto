import subprocess
import os

# Commandos
# [Crackea todas las contraseñas con ambos diccionarios archivo 1] hashcat.exe -m 0 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_1 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force
# [Crea el archivo para el archivo 1 con solo contraseñas en texto plano] hashcat.exe -m 0 -a 0 C:/Users/crist/Desktop/Cripto/Tarea4/archivo_1 C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict --force --show --outfile=simple_output_ar1.txt --outfile-format=2

# Aqui se debe cambiar la direccion de cada una de los archivos (no añadir espacios ni nada mas)

Archivo1 = "C:/Users/crist/Desktop/Cripto/Tarea4/archivo_1"
Archivo2 = "C:/Users/crist/Desktop/Cripto/Tarea4/archivo_2"
Archivo3 = "C:/Users/crist/Desktop/Cripto/Tarea4/archivo_3"
Archivo4 = "C:/Users/crist/Desktop/Cripto/Tarea4/archivo_4"
Archivo5 = "C:/Users/crist/Desktop/Cripto/Tarea4/archivo_5"
Diccionario1 = " C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_1.dict"
Diccionario2 = " C:/Users/crist/Desktop/Cripto/Tarea4/diccionario_2.dict"

os.chdir("C:/Users/crist/Desktop/Cripto/Tarea4/hashcat-6.2.2")
subprocess.run("hashcat.exe -m 0 -a 0 "+Archivo1+Diccionario1+Diccionario2+" --force", shell=True)
subprocess.run("hashcat.exe -m 0 -a 0 "+Archivo1+Diccionario1+Diccionario2+" --force --show --outfile=simple_output_arch1.txt --outfile-format=2", shell=True)
subprocess.run("hashcat.exe -m 10 -a 0 "+Archivo2+Diccionario1+Diccionario2+" --force", shell=True)
subprocess.run("hashcat.exe -m 10 -a 0 "+Archivo2+Diccionario1+Diccionario2+" --force --show --outfile=simple_output_arch2.txt --outfile-format=2", shell=True)
subprocess.run("hashcat.exe -m 10 -a 0 "+Archivo3+Diccionario1+Diccionario2+" --force", shell=True)
subprocess.run("hashcat.exe -m 10 -a 0 "+Archivo3+Diccionario1+Diccionario2+" --force --show --outfile=simple_output_arch3.txt --outfile-format=2", shell=True)
subprocess.run("hashcat.exe -m 1000 -a 0 "+Archivo4+Diccionario1+Diccionario2+" --force", shell=True)
subprocess.run("hashcat.exe -m 1000 -a 0 "+Archivo4+Diccionario1+Diccionario2+" --force --show --outfile=simple_output_arch4.txt --outfile-format=2", shell=True)
subprocess.run("hashcat.exe -m 1800 -a 0 "+Archivo5+Diccionario1+Diccionario2+" --force", shell=True)
subprocess.run("hashcat.exe -m 1800 -a 0 "+Archivo5+Diccionario1+Diccionario2+" --force --show --outfile=simple_output_arch5.txt --outfile-format=2", shell=True)
