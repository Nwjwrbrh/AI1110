import numpy as np
from numpy import random as rn
def div(a,b):
    return a/b

#taking no. of observation as 10000
obs=10000

#x is the number rolled on the die
x=rn.randint(1,7,size=10000)

#y=0(if the man lies) y=1(if the man tells the truth)
y=rn.randint(0,2,size=10000)
z=np.column_stack((x,y))

crt_1=0
crt_2=0
for i in range(0,10000):
    if z[i][0]==6 and z[i][1]==1:
        crt_1+=1
    if z[i][0]!=6 and z[i][1]==0:
        crt_2+=1
print("The experimental probabilty that the reported number 6 is actually a 6 on the die",div(crt_1,crt_1+crt_2))