from io import open

# Crear archivo
texto = "una linea\n"
archivo = open("archivo.txt", "w")
archivo.write(texto)
texto = "otra linea\n"
archivo.write(texto)
texto = "tucutar"
archivo.write(texto)
archivo.close()
