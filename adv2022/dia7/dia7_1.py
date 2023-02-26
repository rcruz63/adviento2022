
tree = []
def tree_append(dir, total):
    tree.append([dir, total])

def ir_a(file, dir) -> int:
    line = file.readline()
    total = 0
    while line:
        line_items = line.split(" ")
        # si la linea es igual "$ cd .."
        if line == "$ cd ..\n":
            tree_append(dir, total)
            return total
            
        # si la linea comienza es igual a "$ cd"
        if line.startswith("$ cd"):
            new_dir = line_items[2].strip()
            total += ir_a(file, new_dir)

        # si line_items[0] es un numero
        if line_items[0].isdigit():
            total += int(line_items[0])

        line = file.readline()
    
    tree_append(dir, total)
    return total

with open('entrada.txt', 'r') as f:
    f.readline()
    ir_a(f, 'root')
    
    total = 0
    for item in tree:
        if item[1] <= 100000:
            print(item[0], item[1])
            total += item[1]
    
    print(total)
    