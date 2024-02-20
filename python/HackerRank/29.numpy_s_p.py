'''
You are given a 2-D array with dimensions X.
Your task is to perform the  tool over axis  and then find the  of that result.

'''
import numpy

n, m = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(n)]
print(numpy.prod(numpy.sum(arr,axis = 0)))
