'''
You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
'''

from itertools import permutations

x,y = list(map(str,input().split()))
x.upper()
x = sorted(x)

c = list(permutations(x,int(y)))
for x in c:
    print(''.join(x),end="\n")
