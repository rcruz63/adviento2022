from os import path

def main():
    lista = []
    total = 0
    pathbase = path.dirname(__file__)
    with open(path.join(pathbase, 'entrada.txt')) as f:
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

main()