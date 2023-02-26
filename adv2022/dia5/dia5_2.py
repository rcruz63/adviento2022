WORDS = ['WDGBHRV',
'JNGCRF',
'LSFHDNJ',
'JDSV',
'SHDRQWNV',
'PGHCM',
'FJBGLZHC',
'SJR',
'LGSRBNVM']

def to_list(words) -> list:
    """Convert a list of words to a list of stacks"""
    stcks = []
    for word in words:
        aux = list(word)
        stcks.append(aux)
    return stcks

def move(stack, n, from_index, to_index): 
    """Move n elements from stack[fromIndex] to stack[toIndex]"""
    aux = stack[from_index][-n:] 
    for c in aux:
        stack[to_index].append(c)
        stack[from_index].pop()

def main():
    """Main function"""
    stacks = to_list(WORDS)
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