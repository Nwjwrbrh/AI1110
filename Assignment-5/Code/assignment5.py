"""Question: A red and a black die are rolled
Find the conditional probability of obtaining a sum greater than 9, given that the black die resulted in a 5.
Find the conditional probability of obtaining the sum 8, given that the red die resulted in a number less than 4"""
def div(x,y):
    return x/y
#sample size
N=36
cnt_1=0
cnt_2=0
cnt_3=0
cnt_4=0
for i in range(1,7):
    for j in range(1,7):
        if i == 5 and i + j > 9:
            cnt_1=cnt_1+1
        if i + j == 8 and j < 4:
            cnt_2=cnt_2+1
        if i == 5:
            cnt_3=cnt_3+1
        if j < 4:
            cnt_4=cnt_4+1
pr_1=div(cnt_1,cnt_3)
pr_2=div(cnt_2,cnt_4)
print('The probability for the first condition',pr_1)
print('The probability for the second condition',pr_2)