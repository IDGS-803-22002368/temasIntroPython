from io import open

archivo = open("archivo.txt", "r")

texto = archivo.read()

print(texto)

archivo.seek(0)

texto = archivo.readlines()

print(texto)

archivo.seek(0)

linea = archivo.readline()

print(linea)

while linea != "":
    print(linea)
    linea = archivo.readline()

archivo.close()
