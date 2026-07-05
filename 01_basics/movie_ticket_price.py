age = int(input("Please enter your age: "))
day = input("Please enter the day of the week: ")


if age < 0:
    print("Age cannot be negative. Please enter a valid age.")
else:
    if age < 13:
        print("You are a child.")
        price = 5
    elif age >=13 and age < 20:
        print("You are a teenager.")
        price = 7
    else:
        print("You are an adult.")
        price = 10

if day == "wednesday":
    actual_price = price - 2
    print("price after discount is: ", actual_price)
else:
    print("price is: ", price)