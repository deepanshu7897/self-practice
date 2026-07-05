number = int (input("Please enter a number: "))
for i in range (1, number + 1):
    if i == 5:
        continue
    i = number * i
    print(number, "x", i // number, "=", i)