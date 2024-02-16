'''
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

Find the total number of distinct country stamps.

Input Format
'''
n = int(input())
i = 0
s = set()
for i in range(n): 
    c = input()
    s.add(c)
        
print(len(s))
