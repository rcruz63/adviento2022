import numpy as np


def abajo(forest, visibles, x):
    high = forest[0, x]
    if high == 9:
        return
    for y in range(1, forest.shape[1] - 1):
        if forest[y, x] == 9:
            visibles[y, x] = 1
            return
        if forest[y, x] > high:
            high = forest[y, x]
            visibles[y, x] = 1
    return


def izquierda(forest, visibles, x):
    top = forest.shape[1] - 1
    # * print("top:", top)
    high = forest[x, top]
    # * print("high:", high)
    if high == 9:
        return
    for y in range(1, top):
        k = top - y
        # * print("k:", k, "x:", x, "forest[x, k]:", forest[x, k])
        if forest[x, k] == 9:
            visibles[x, k] = 1
            return
        if forest[x, k] > high:
            high = forest[x, k]
            # * print("high:", high)
            visibles[x, k] = 1
    return


def derecha(forest, visibles, x):
    high = forest[x, 0]
    if high == 9:
        return
    for y in range(1, forest.shape[1] - 1):
        if forest[x, y] == 9:
            visibles[x, y] = 1
            return
        if forest[x, y] > high:
            high = forest[x, y]
            visibles[x, y] = 1
    return


def arriba(forest, visibles, x):
    top = forest.shape[0] - 1
    high = forest[top, x]
    for y in range(1, top):
        k = top - y
        # * print("k:", k, "x:", x, "forest[k, x]:", forest[k, x])
        if forest[k, x] == 9:
            visibles[k, x] = 1
            return
        if forest[k, x] > high:
            # * print("high:", high)
            # * print("forest[k, x]", forest[k, x])
            high = forest[k, x]
            visibles[k, x] = 1
    return


def dia8_1(forest):
    visibles = np.zeros(forest.shape)
    mx = forest.shape[0] - 1
    for i in range(forest.shape[0]):
        visibles[i, 0] = 1
        visibles[0, i] = 1
        visibles[mx, i] = 1
        visibles[i, mx] = 1
        if i == 0 or i == mx:
            continue
        abajo(forest, visibles, i)
        derecha(forest, visibles, i)
        arriba(forest, visibles, i)
        izquierda(forest, visibles, i)

    # * print(forest)
    # * print(visibles)
    print(np.sum(visibles))


def left(forest, x, y) -> int:
    izq = 0
    for i in range(y):
        izq += 1
        if forest[x, y-(i+1)] >= forest[x, y]:
            return izq
    return izq
        

def right(forest, x, y) -> int:
    der = 0
    for i in range(forest.shape[1] - y -1):
        der += 1
        ##* print("Right:", der, ", x:", x, ", y:", y, ", i:", i)
        if forest[x, y+i+1] >= forest[x, y]:
            return der
    return der

def up(forest, x, y) -> int:
    up = 0
    for i in range(x):
        up += 1
        if forest[x-(i+1), y] >= forest[x, y]:
            return up
    return up

def down(forest, x, y) -> int:
    down = 0
    for i in range(forest.shape[0] - x -1):
        down += 1
        if forest[x+i+1, y] >= forest[x, y]:
            return down
    return down


def dia8_2(forest):
    # Generar una matriz de puntuaciones
    scores = np.zeros(forest.shape)
    for i in range(forest.shape[0]):
        if i == 0 or i == (forest.shape[0] - 1):
            scores[i, :] = 0
            continue
        for j in range(forest.shape[1]):
            if j == 0 or j == (forest.shape[1] - 1):
                scores[i, j] = 0
                continue
            scores[i, j] = up(forest, i, j)*down(forest, i, j)*left(forest, i, j)*right(forest, i, j)
    ##* print(scores)
    print(np.max(scores))
    ##* print(forest)
    ##* print(scores)


def main(file="entrada.txt"):

    forest = np.genfromtxt(file, delimiter=1, dtype=int)
    # * print(forest.shape)
    dia8_1(forest)
    dia8_2(forest)


if __name__ == "__main__":
    main("entrada.txt")
