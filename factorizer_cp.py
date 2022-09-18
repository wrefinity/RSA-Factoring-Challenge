#!/usr/bin/python3
import sys
import ctypes
from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp


def unix_time(func):
    '''Returns `real`, `sys` and `user` elapsed time just like UNIX's command time
    1. calculate the amount of used CPU-time
    '''
    start_time, start_res = timestamp(), resource_usage(RUSAGE_SELF)
    func()
    end_res, end_time  = resource_usage(RUSAGE_SELF), timestamp()
  
    return "\nreal: {}\nuser: {}\nsys: {}\n".format(
        end_time - start_time,
        end_res.ru_utime - start_res.ru_utime,
        end_res.ru_stime - start_res.ru_stime)

def print_factors():
    fun = ctypes.CDLL("./lib_factors_functions.so")
    fun.trial_division.argtypes = [ctypes.c_long]
    with open(sys.argv[1], 'r') as src:
        prime = src.readline()
        while prime  != '':
            num = int(prime)
            fun.trial_division(num)
            prime = src.readline()
