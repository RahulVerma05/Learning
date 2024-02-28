'''
You are given a string .
Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.
'''
from itertools import combinations_with_replacement

x,y =input().split()
y = int(y)
x = sorted(x)
a = list(combinations_with_replacement(x,y))

for i in a:
    print(''.join(i),end='\n')
