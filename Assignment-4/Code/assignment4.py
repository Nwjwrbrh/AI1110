import math
def div(a,b):
    return a/b
print('Lets assume there are 24 balls in a bag with 2 two colours blue and green')
print('Please enter the probabilty of randomly drawing a green ball')
num=int(input('numerator :'))
den=int(input('denominator :'))
x= div(num,den)
y=(1-x)*24
print('then the number of blue balls present is',y)