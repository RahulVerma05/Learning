'''
You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.

'''


n = int(input())

for _ in range(n):
    a = input()
    s1 = set(input().split())
    b = input()
    s2 = set(input().split())
    print(s1.issubset(s2))
