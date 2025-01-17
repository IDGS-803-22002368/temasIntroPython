x = []  # Lista
y = (1, 2, 3, 4, 5)  # Tupla

# Diferencia entre tupla y lista
# Tupla: Inmutable
# Lista: Mutable
# Ejemplo
x.append(1)
x.append(2)

x.append(y)
print(x)

# y.append(6)  # Error

# print(x[3]) # Error

for i in y:
    print(i)
