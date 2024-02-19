'''
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.
'''
import numpy

def arrays(arr):
    arr = numpy.array(arr,float)[::-1]
    # complete this function
    # use numpy.array
    return arr
