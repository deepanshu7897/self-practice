password = input("Enter your password: ")
if len(password) < 8 or password.isalpha() == True or password.isdigit() == True or password.isalnum() == True:
    print("Password is weak. Please enter a stronger password.")
else :
    print("Password is strong.")    