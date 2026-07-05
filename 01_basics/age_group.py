age = int(input("Please enter your age: "))
if age < 0:
    print("Age cannot be negative. Please enter a valid age.")
else:
    if age < 13:
        print("You are a child.")
    elif age >=13 and age < 20:
        print("You are a teenager.")
    else:
        print("You are an adult.")