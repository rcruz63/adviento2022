import monkey

if __name__ == '__main__':
    # Monkey(id, items, operation, test, worried, noworried)
    m1 = monkey.Monkey(1, [1, 2, 3], lambda x: x, 0, 0, 0)
    m2 = monkey.Monkey(2, [4, 5, 6], lambda x: x, 0, 0, 0)
    print(m1)
    print(m2) 