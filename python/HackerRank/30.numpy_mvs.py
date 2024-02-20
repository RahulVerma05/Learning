'''
You are given a 2-D array of size X.
Your task is to find:

The mean along axis 
The var along axis 
The std along axis 
Input Format
'''
import numpy

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

print(numpy.mean(arr,axis = 1))
print(numpy.var(arr,axis = 0))
print(round(numpy.std(arr,axis = None),11))
