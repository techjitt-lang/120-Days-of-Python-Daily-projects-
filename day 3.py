#Simple Calculator for type casting 
#No of inputs: 2
#Type casting 
print('Press 1 For Addition')
print('Press 2 For Substraction')
print('Press 3 For Multiplication')
print('Press 4 For Division')
ask = int(input('Choose the Option: '))
if ask < 1 or ask > 4:
    print('Invalid Choice')
else:
    Num = str(input('Enter Your 1st Number: '))
    Numb = str(input('Enter your 2nd Number: '))
    Numb = int(Numb)
    Num = int(Num)
    if ask == 1:
        print('The Sum of Numbers 1 and 2 is : ',(Num + Numb))
    elif ask == 2:
        print('The Difference of Number 1 and 2 is : ',(Num - Numb))
    elif ask == 3:
        print('Multiplication of Number 1 and 2 is : ',(Num * Numb))
    elif ask == 4:    
        if Numb == 0:
            print('Denominator can not be 0')
        else:
            print('Division Of Number 1 and 2 is : ',(float(Num/Numb)))

