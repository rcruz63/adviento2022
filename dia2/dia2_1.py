total = 0
with open('entrada.txt') as f:
    for linea in f:
        j = linea.split()
        print(j)
        if ((j[0] == 'A') & (j[1] == 'X')):
            print ("Piedra & Piedra = empate")
            total += 1 + 3
        elif ((j[0] == 'A' ) & ( j[1] == 'Y')):
            print ("Piedra & Papel = Victoria")
            total += 2 + 6
        elif ((j[0] == 'A' ) & ( j[1] == 'Z')):
            print ("Piedra & Tijera = Derrota")
            total += 3 + 0
        elif ((j[0] == 'B' ) & ( j[1] == 'X')):
            print("Papel & Piedra = Derrota")
            total += 1 + 0
        elif ((j[0] == 'B' ) & ( j[1] == 'Y')):
            print("Papel & Papel = Empate")
            total += 2 + 3
        elif ((j[0] == 'B' ) & ( j[1] == 'Z')):
            print("Papel y tijera = Vistoria")
            total += 3 + 6
        elif ((j[0] == 'C' ) & ( j[1] == 'X')):
            print ("Tijera & Roca = Victoria")
            total += 1 + 6
        elif ((j[0] == 'C' ) & ( j[1] == 'Y')):
            print("Tijera & Papel = Derrota")
            total += 2 + 0
        elif ((j[0] == 'C' ) & ( j[1] == 'Z')):
            print("Tijera y Tijera = Empate")
            total += 3 + 3

print(total)
            