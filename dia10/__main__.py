import dia10

if __name__ == "__main__":

    ciclos = dia10.construir_ciclos("./dia10/entrada.txt")
    print(dia10.dia10_1(ciclos))
    CRT = dia10.dia10_2(ciclos)
    for row in CRT:
        print(row)