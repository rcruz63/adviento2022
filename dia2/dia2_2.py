total = 0
with open('entrada.txt') as f:
    for linea in f:
        j = linea.split()
        print(j)
        if ((j[0] == 'A') & (j[1] == 'X')):
            print ("Piedra & Perder = Tijeras")
            total += 3 + 0
        elif ((j[0] == 'A' ) & ( j[1] == 'Y')):
            print ("Piedra & Empate = Piedra")
            total += 1 +  3
        elif ((j[0] == 'A' ) & ( j[1] == 'Z')):
            print ("Piedra & Victoria = Papel")
            total += 2 + 6
        elif ((j[0] == 'B' ) & ( j[1] == 'X')):
            print("Papel & Perder = Piedra")
            total += 1 + 0
        elif ((j[0] == 'B' ) & ( j[1] == 'Y')):
            print("Papel & Empate = Papel")
            total += 2 + 3
        elif ((j[0] == 'B' ) & ( j[1] == 'Z')):
            print("Papel y Victoria = Tijera")
            total += 3 + 6
        elif ((j[0] == 'C' ) & ( j[1] == 'X')):
            print ("Tijera & perder = Papel")
            total += 2 + 0
        elif ((j[0] == 'C' ) & ( j[1] == 'Y')):
            print("Tijera & Empate = Tijera")
            total += 3 + 3
        elif ((j[0] == 'C' ) & ( j[1] == 'Z')):
            print("Tijera y Victoria = Roca")
            total += 1 + 6

print(total)
            