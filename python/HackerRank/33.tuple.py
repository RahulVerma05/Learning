'''
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t).
'''

#pyp3
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    
    print(hash(t))

#python3 not working

n = int(input())
t = tuple(map(int,tuple(input().split(maxsplit=n))))

print(hash(t))
