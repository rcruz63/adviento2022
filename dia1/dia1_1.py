lista = []
total = 0
with open('entrada.txt') as f:
    for linea in f:
        if (linea == "\n"):
            lista.append(total)
            total = 0
        else:
            total += int(linea, 10)

lista.sort(reverse=True)

print(lista[0])
print(lista[1])
print(lista[2])

print(lista[0]+lista[1]+lista[2])