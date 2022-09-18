#!/usr/bin/python3
import sys
import ctypes
from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp


def unix_time(function):
    '''Return `real`, `sys` and `user` elapsed time, like UNIX's command `time`
    calculates the amount of used CPU-time
    '''
    start_time, start_res = timestamp(), resource_usage(RUSAGE_SELF)
    function()
    end_res, end_time = resource_usage(RUSAGE_SELF), timestamp()

    return "\nreal: {}\nuser: {}\nsys: {}".format(
        end_time - start_time,
        end_res.ru_utime - start_res.ru_utime,
        end_res.ru_stime - start_res.ru_stime)


def print_factors():
    func = ctypes.CDLL("./lib_factors_functions.so")
    func.trial_division.argtypes = [ctypes.c_long]
    with open(sys.argv[1], 'r') as src:
        prime = src.readline()
        while prime != '':
            num = int(prime)
            func.trial_division(num)
            prime = src.readline()
