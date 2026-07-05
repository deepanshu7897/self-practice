distance = int(input("enter the distance "))
if distance < 3 :
    transport = 'walk'
elif distance >= 3 and distance < 10 :
    transport = 'bicycle'
elif distance >= 10 and distance < 100 :
    transport = 'bus'
elif distance >= 100 and distance < 1000 :
    transport = 'train'
else:
    transport = 'airplane'
print("the mode of transport is: ", transport)        