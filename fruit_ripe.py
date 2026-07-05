fruit = input("Enter the name of a fruit: ")
colour = input("Enter the colour of the fruit: ")
if fruit == 'apple':
    if colour=='red':
        print('The fruit is a ripe apple.')
    elif colour=='brown':
        print('the fruit is overgrown')
    else :
        print(' the fruit is unripe')
elif fruit == 'banana':
    if colour=='yellow':
        print('The fruit is a ripe banana.')
    elif colour=='green':
        print('the fruit is unripe')
    else :
        print(' the fruit is overgrown')   
else :
    print('the fruit entry is not found')             


    