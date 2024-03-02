'''
You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.

Input Format

A single line of input containing  space separated integers.

'''
import numpy

arr = list(map(int,input().split()))

a = numpy.array(arr)

b = numpy.reshape(a,(3,3))

print(b)
