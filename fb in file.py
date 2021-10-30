filename = "fizzbuzz.txt"

file_fb = open(filename, "r")

for line in file_fb:
    fizz, buzz, c = line.split()
    fizz = int(fizz)
    buzz = int(buzz)
    c = int(c)

    for x in (range(1, c + 1)):
        if x % fizz == 0 and x % buzz == 0:
            print('FB', end=" ")
        elif x % fizz == 0:
            print("B", end=' ')
        elif x % buzz == 0:
            print("F", end=' ')
        else:
            print(x, end=' ')
    print()
file_fb.close()
