'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
'''
a = '.|.'
c = '-'
l,n = map(int,input().split())
# Top half
for i in range(l//2):
    print((a*i).rjust(n//2-1,c)+a+(a*i).ljust(n//2-1,c))
#centre
print(('WELCOME').center(n,c))
#bottom half
for i in reversed(range(l//2)):
    print((a*i).rjust(n//2-1,c)+a+(a*i).ljust(n//2-1,c))
