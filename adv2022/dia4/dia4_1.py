total = 0
with open('entrada.txt', 'r') as f:
        for line in f:
            first, second = line.split(",")
            firstmin, firstmax = first.split("-")
            secondmin, secondmax = second.split("-")
            

            if (int(firstmin) <= int(secondmin) and int(firstmax) >= int(secondmax)) or (int(firstmin) >= int(secondmin) and int(firstmax) <= int(secondmax)):
                ##* print(firstmin, firstmax, secondmin, secondmax)
                total += 1

print(total)








            