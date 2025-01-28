from io import open
import os


class Diccionario:

    def __init__(self):
        self.diccionario = {}
        self.cargar_diccionario()

    def cargar_diccionario(self):
        self.diccionario = {}
        archivo = open("diccionario.txt", "r")
        for linea in archivo:
            linea = linea.replace("\n", "")
            palabra_espanol, palabra_ingles = linea.split(" : ")
            self.diccionario[palabra_espanol.lower()] = palabra_ingles.lower()
        archivo.close()
    
    def agregar_palabra(self, palabra_ingles, palabra_espanol):
        archivo = open("diccionario.txt", "a")
        archivo.write(palabra_espanol + " : " + palabra_ingles + "\n")
        archivo.close()
        self.cargar_diccionario()
        print(f"La palabra {palabra_ingles} con traduccion {palabra_espanol} ha sido agregada al diccionario")
        
    def buscar_palabra_espanol(self, palabra_espanol):
        self.cargar_diccionario()
        palabra_buscar = palabra_espanol.lower()
        if palabra_buscar in self.diccionario:
            print(f"La traducción de {palabra_espanol} es {self.diccionario[palabra_buscar]}")
        else:
            print("La palabra no se encuentra en el diccionario")
    
    def buscar_palabra_ingles(self, palabra_ingles):
        self.cargar_diccionario()
        palabra_buscar = palabra_ingles.lower()
        if palabra_buscar in self.diccionario.values():
            for palabra, traduccion in self.diccionario.items():
                if traduccion == palabra_buscar:
                    print(f"La traducción de {palabra_ingles} es {palabra}")
        else:
            print("La palabra no se encuentra en el diccionario")


def menu():
    os.system("cls")
    obj = Diccionario()
    while True:
        print('1: Agregar palabra')
        print('2: Buscar palabra')
        print('3: Salir')
        opcion = input("Elige una opcion: ")
            
        if opcion == '1':
            os.system("cls")
            palabra_ingles = input("Ingresa la palabra en ingles: ")
            palabra_espanol = input("Ingresa la palabra en español: ")
            if palabra_espanol == "":
                print("La palabra en español no puede estar vacía")
            elif palabra_ingles == "":
                print("La palabra en inglés no puede estar vacía")
            else:
                obj.agregar_palabra(palabra_ingles, palabra_espanol)
        elif opcion == '2':
            os.system("cls")
            print('1: Buscar palabra en español')
            print('2: Buscar palabra en ingles')
            opcion = input("Elige una opcion: ")
            if opcion == '1':
                os.system("cls")
                palabra_espanol = input("Ingresa la palabra en español: ")
                obj.buscar_palabra_espanol(palabra_espanol)
            elif opcion == '2':
                os.system("cls")
                palabra_ingles = input("Ingresa la palabra en ingles: ")
                obj.buscar_palabra_ingles(palabra_ingles)
            else:
                print("Opción no válida")
        elif opcion == '3':
            print("Adios")
            os.system("cls")
            break
        else:
            print("Opción no válida")


def main():
    menu()


if __name__ == "__main__":
    main()
