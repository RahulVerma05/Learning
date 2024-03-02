'''
You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .

Input Format

The first line contains space separated integers ,  and .
The next  lines contains the space separated elements of the  columns.
After that, the next  lines contains the space separated elements of the  columns.
'''
import numpy

n,m,p = map(int,input().split())
arr_n = [list(map(int,input().split())) for _ in range(n)]
arr_m = [list(map(int,input().split())) for _ in range(m)]

an = numpy.array(arr_n)
am = numpy.array(arr_m)
print(numpy.concatenate((arr_n,arr_m),axis = 0))
