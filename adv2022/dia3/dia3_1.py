# quiero leer el archivo de texto y procesarlo linea a linea

def main() -> int:
    total = 0
    # leer el archivo de texto
    with open('entrada.txt', 'r') as f:
        for line in f:
            first = line[:len(line)//2]
            second = line[len(line)//2:]
            ##* print(first, second)
            # para cada caracter en first
            for c in first:
                # buscar si está en second
                if c in second:
                    # sumar a total el valor de c
                    # si es mayuscula, restar ord('A) + 1
                    # si es minuscula, restar ord('a') + 1
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