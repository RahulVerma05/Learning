'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''
if __name__ == '__main__':
    N = int(input())
    l = []
    i = 0
    for i in range(N):
        c = input().split()
        if c[0] == 'insert':
            l.insert(int(c[1]),int(c[2]))
        elif c[0] == 'remove':
            l.remove(int(c[1]))
        elif c[0] == 'append':
            l.append(int(c[1]))
        elif c[0] == 'sort':
            l.sort()
        elif c[0] == 'pop':
            l.pop(-1)
        elif c[0] == 'reverse':
            l.reverse()
        elif c[0] == 'print':
            print(l)
