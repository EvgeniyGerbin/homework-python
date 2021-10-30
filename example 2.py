# маленький скрипт на проверку совпадений 3 чисел
a = int(input())  # enter the first number
b = int(input())  # enter the second number
c = int(input())  # enter the third number
if a == b == c:    # math check
    print("3")
elif a == b or b == c or c == a:
    print("2")
else:
    print("0")
