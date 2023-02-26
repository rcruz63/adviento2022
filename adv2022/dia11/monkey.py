# definir una clase mono
# atributos: id: int, items:list, operation: lambda, test: int, worried: int, noworried:int
class Monkey:
    id: int
    items: list
    operation = lambda x: x
    test: int
    worried: int
    noworried: int
    # constructor
    def __init__(self, id, items, operation, test, worried, noworried):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.worried = worried
        self.noworried = noworried
