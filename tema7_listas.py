lista1 = []
lista2 = [1, 2, 3, 4, 5]
lista3 = ["a", "b", "c", "d", "e"]
lista4 = [1, "a", 2, "b", 3, "c"]
lista5 = [1.1, 2.2, 3.3, 4.4, 5.5]

# print("\n", lista1, "\n", lista2, "\n", lista3, "\n", lista4, "\n", lista5, "\n") # Imprime las listas
# print("\n", type(lista1), "\n", type(lista2), "\n", type(lista3), "\n", type(lista4), "\n", type(lista5), "\n") # Imprime el tipo de dato de las listas

# print("\n", lista2[0], "\n", lista3[1], "\n", lista4[2], "\n", lista5[3], "\n") # Acceso a los elementos de la lista
# print("\n", len(lista2), "\n", len(lista3), "\n", len(lista4), "\n", len(lista5), "\n") # len() devuelve la longitud de la lista

# print(lista1[3])  # IndexError: list index out of range

# print(lista2[0:3]) # Acceso a un rango de elementos de la lista
# print(lista3[1:4:2]) # Acceso a un rango de elementos de la lista con un salto de 2
# print(lista4[::2]) # Acceso a un rango de elementos de la lista con un salto de 2

# lista1.append(1)  # Agrega un elemento al final de la lista
# lista1.append(2)
# print(lista1)

# lista1.pop(1)  # Elimina un elemento de la lista por su índice
# print(lista1)

# print(lista2)
# lista2.sort()  # Ordena la lista
# print(lista2)

print(lista3)
lista3.sort(reverse=True)  # Ordena la lista en orden inverso
print(lista3)