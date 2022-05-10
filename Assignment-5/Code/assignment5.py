"""Question: A red and a black die are rolled
Find the conditional probability of obtaining a sum greater than 9, given that the black die resulted in a 5.
Find the conditional probability of obtaining the sum 8, given that the red die resulted in a number less than 4"""
import numpy as np
from numpy import random as rn

#div
def div(x,y):
    return x/y    

#sample size
N=36

#for theoritical probability
cnt_1=0
cnt_2=0
cnt_3=0
cnt_4=0
for i in range(1,7):
    for j in range(1,7):
        if i == 5 and i + j > 9:
            cnt_1+=1 
        if i + j == 8 and j < 4:
            cnt_2+=1
        if i == 5:
            cnt_3+=1
        if j < 4:
            cnt_4+=1
tp_1=div(cnt_1,cnt_3)
tp_2=div(cnt_2,cnt_4)

#for experimental probability using random variable
#I just took the no. of observation be 10000
obs=10000
crt_1=0
crt_3=0
x=rn.randint(1,7,size = obs)
y=rn.randint(1,7,size = obs)
z=np.column_stack((x,y))
print(z)
for i in range(0,obs):
    if z[i][0]==5 and  z[i][0]+z[i][1]>9:
        crt_1+=1
    if z[i][1]<4 and z[i][0]+z[i][1]==8:
        crt_3+=1
crt_2=np.count_nonzero(x==5)
crt_4=np.count_nonzero(y<4)
ep_1=div(crt_1,crt_2)
ep_2=div(crt_3,crt_4)

#printing the values
print('The theoritical probability for the first condition and the second condition is',tp_1,'and',tp_2)
print('The experimental probability for the first condition and the second condition is',ep_1,'and',ep_2)

#kept this if this is the correct one
'''x=rn.randint(0,37)
y=rn.randint(0,37)
ep_1=div(x,N)
ep_2=div(y,N)
print('The experimental probability for the first condition and the second condition is',ep_1,'and',ep_2)'''