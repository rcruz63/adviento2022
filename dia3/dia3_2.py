# quiero leer el archivo de texto y procesarlo linea a linea

def main() -> int:
    total = 0
    i = 0
    # leer el archivo de texto
    with open('entrada.txt', 'r') as f:
        for line in f:
            if i == 0:
                i += 1
                first = line
            elif i == 1:
                i += 1
                second = line
            elif i == 2:
                third = line
                i=0
                for c in first:
                    if c in second and c in third:
                        if c.isupper():
                            total += ord(c) - ord('A') + 27
                            ##* print(c, " prioridad: ", ord(c) - ord('A') + 27)
                        else:
                            total += ord(c) - ord('a') + 1
                            ##* print(c, " prioridad: ", ord(c) - ord('a') + 1)
                        ##* print(total)
                        break
    return total
TOTAL = main()
print(TOTAL)