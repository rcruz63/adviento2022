WORDS = ['WDGBHRV',
'JNGCRF',
'LSFHDNJ',
'JDSV',
'SHDRQWNV',
'PGHCM',
'FJBGLZHC',
'SJR',
'LGSRBNVM']

def toList(words) -> list:
    stcks = []
    for word in words:
        aux = list(word)
        stcks.append(aux)
    return stcks

def move(stack, n, fromIndex, toIndex): 
    for i in range(n):
        stack[toIndex].append(stack[fromIndex].pop())

def main():
    stacks = toList(WORDS)
    j = 0
    with open('entrada.txt', 'r') as f:
        for line in f:
            instructions = line.split(" ")
            move(stacks, int(instructions[1]), int(instructions[3]) - 1, int(instructions[5]) - 1)
            j += 1
            ##* print(j," -> " , stacks)
    
    
    aux = []
    for stack in stacks: 
        aux.append(stack.pop())
    print("".join(aux))



if __name__ == '__main__':
    main()