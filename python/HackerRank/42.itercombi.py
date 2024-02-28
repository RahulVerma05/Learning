'''
You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.
'''
from itertools import combinations

x,y = input().split()
y = int(y)
x.upper()
x = sorted(x)

for i in range(1,y+1):
    a = list(combinations(x,i))
    for i in a:
        print(''.join(i),end='\n')
