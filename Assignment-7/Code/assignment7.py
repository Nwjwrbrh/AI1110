import numpy as np
from numpy import random as rn
def div(a,b):
    return a/b

#observation
obs=10000

#taking total time to be 60 meaning (0,60)
T=60

#x represents the time interval (x-1,x) like 1 means (0,1)
x=rn.randint(1,61,size=obs)

#finding the probability of the call coming at the time interval (20,40)
z=np.empty(obs)
for i in range(0,obs):
    if x[i]<41 and x[i]>20:
        z[i]=1
    else:
        z[i]=0

#probability
crt=np.count_nonzero(z==1)
print('THe erperimental value that the call occurs at bthe interval (20,40) is', div(crt,obs))