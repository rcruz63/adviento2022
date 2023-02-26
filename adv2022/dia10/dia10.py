def pr_cl(i, j, l, c):
    print(i, "-", j, ":", l, ": ", c[i])

def print_ciclos(ln, i, cl):
    if len(cl) == 21:
        pr_cl(20, i, ln, cl)
    if len(cl) == 61:
        pr_cl(60, i, ln, cl)
    if len(cl) == 101:
        pr_cl(100, i, ln, cl)
    if len(cl) == 141:
        pr_cl(140, i, ln, cl)
    if len(cl) == 181:
        pr_cl(180, i, ln, cl)
    if len(cl) == 221:
        pr_cl(220, i, ln, cl)

def construir_ciclos(file="test.txt") -> list:
    X = 1
    ciclos = []
    with open(file) as f:
        for line in f:
            if line[:4] != "noop":
                _, val = line.split(" ")
                ciclos.append(X)
                ciclos.append(X)
                X += int(val)
                ##* print_ciclos(line.strip(), 1, ciclos)
            else:
                ciclos.append(X)
                ##* print_ciclos(line.strip(), 2, ciclos)
    return ciclos

def dia10_1(ciclos) -> int:
    return 20*ciclos[19]+60*ciclos[59]+100*ciclos[99]+140*ciclos[139]+180*ciclos[179]+220*ciclos[219]


def dia10_2(ciclos) -> list:
    CRT = ["........................................",
           "........................................",
           "........................................",
           "........................................",
           "........................................",
           "........................................"]
    
    for i, sprite in enumerate(ciclos):
        pixel = i % 40
        row = i // 40
        if (pixel >= sprite - 1) and (pixel <= sprite + 1):
            CRT[row] = CRT[row][:pixel] + "#" + CRT[row][pixel+1:]
    
    return CRT

if __name__ == "__main__":
    ciclos = construir_ciclos("entrada.txt")
    print(dia10_1(ciclos))
    CRT = dia10_2(ciclos)
    for row in CRT:
        print(row)