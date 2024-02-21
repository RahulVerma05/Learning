'''
You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results.
'''

import numpy

n,m = map(int,input().split())
arr = numpy.array([input().split() for _ in range(n)],int)

print(numpy.transpose(arr))
print(arr.flatten())
