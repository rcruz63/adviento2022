

# Funcion para comprobar si hay caracteres repetidos en una lista
def check_repeated_characters(list):
    for i in list:
        if list.count(i) > 1:
            return True
    return False


def main():
    # Leer un archivo caracter a caracter
    with open('entrada.txt', 'r') as f:
        # Leer el primer caracter
        char = f.read(1)
        # crear lista vacía
        list = []
        # Mientras no sea el final del archivo
        while char != '':
            # añadir caracter a la lista
            list.append(char)
            if len(list) >= 14:
                # comprobar si hay caracteres repetidos
                if not (check_repeated_characters(list[-14:])):
                    print("No hay caracteres repetidos:", list[-14:], len(list))
                    break
            # leer siguiente caracter
            char = f.read(1)
            

# main
if __name__ == '__main__':
    main()