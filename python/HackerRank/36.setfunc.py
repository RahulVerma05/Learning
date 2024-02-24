'''
You have a non-empty set , and you have to execute  commands given in  lines.

The commands will be pop, remove and discard.
'''
n = int(input())
s = set(map(int, input().split()))
x = int(input())
for _ in range(x):
    c = input().split()
    if c[0] == 'remove':
        s.remove(int(c[1]))
    elif c[0] == 'discard':
        s.discard(int(c[1]))
    elif c[0] == 'pop':
        s.pop()
        
print(sum(s))
