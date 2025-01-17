import os


def suma():
    print("\nSUMA")
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    print(f"Resultado: {n1 + n2}")


def resta():
    print("\nRESTA")
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    print(f"Resultado: {n1 - n2}")


def multiplicacion():
    print("\nMULTIPLICACIÓN")
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    print(f"Resultado: {n1 * n2}")


def division():
    print("\nDIVISIÓN")
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    print(f"Resultado: {n1 / n2}")


def menu():
    while True:
        os.system('cls')
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == '1':
            suma()
        elif opcion == '2':
            resta()
        elif opcion == '3':
            multiplicacion()
        elif opcion == '4':
            division()
        elif opcion == '5':
            print("Adios")
            break
        else:
            print("Opción no válida")
            
        input("Enter para continuar")


if __name__ == "__main__":
    menu()
