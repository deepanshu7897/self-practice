number = int (input("Please enter a number: "))
sum_even = 0
sum_odd = 0
for i in range (0, number + 1):
    if i % 2 == 0:
        sum_even += i
    else :
        sum_odd += i

print("The sum of even numbers from 0 to", number, "is:", sum_even)
print("The sum of odd numbers from 0 to", number, "is:", sum_odd)
