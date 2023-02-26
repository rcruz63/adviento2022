# Si es _main_: Ejecuta el código

def move_tail (h, t) -> list:
    result = [t[0], t[1]]
    dif_x = h[0] - t[0]
    dif_y = h[1] - t[1]
    
    if abs(dif_x) < 2 and abs(dif_y) < 2:
        return result
    
    if dif_x > 0:
        result[0] += 1
    elif dif_x < 0:
        result[0] -= 1
    if dif_y > 0:
        result[1] += 1
    elif dif_y < 0:
        result[1] -= 1

    return result


def dia9_1():
    head = [0,0]
    tail = [0,0]
    tails = [tail]

    # leer el archivo entrada.txt
    with open("entrada.txt", "r") as f:
        for line in f:
            dir, dist = line.split(" ")
            dist = int(dist)
            for i in range(dist):
                if dir == "R":
                    head[1] += 1
                elif dir == "L":
                    head[1] -= 1
                elif dir == "U":
                    head[0] += 1
                elif dir == "D":
                    head[0] -= 1
                else:
                    raise Exception("Invalid direction")
                tail = move_tail (head, tail)
                if tail not in tails:
                    tails.append(tail)


    ##* print(tails)
    print(len(tails))

def dia9_2():
    rope = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]] 

    tails = [rope[-1]]

    # leer el archivo entrada.txt
    with open("entrada.txt", "r") as f:
        for line in f:
            dir, dist = line.split(" ")
            dist = int(dist)
            for i in range(dist):
                if dir == "R":
                    rope[0][1] += 1
                elif dir == "L":
                    rope[0][1] -= 1
                elif dir == "U":
                    rope[0][0] += 1
                elif dir == "D":
                    rope[0][0] -= 1
                else:
                    raise Exception("Invalid direction")

                for i in range(1, len(rope)):
                    rope[i] = move_tail(rope[i-1], rope[i])
                
                if rope[-1] not in tails:
                    tails.append(rope[-1])


    ##* print(tails)
    print(len(tails))




if __name__ == "__main__":
    dia9_1()
    dia9_2()