size = input("What size coffee would you like? (small, medium, large): ")
expresso = input("Would you like an expresso shot? (yes or no): ")
if expresso =='yes':
    size = size + " expresso"
else :
    size = size + " regular"
print("You have ordered a " + size + " coffee.")     
