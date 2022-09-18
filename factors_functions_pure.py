#!/usr/bin/python3
import sys

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp


def unix_time(function):
    '''Return `real`, `sys` and `user` elapsed time, like UNIX's command `time`
    calculates the amount of used CPU-time
    '''
    start_time, start_res = timestamp(), resource_usage(RUSAGE_SELF)
    function()
    end_res, end_time = resource_usage(RUSAGE_SELF), timestamp()

    return "\nreal: {}\nuser: {}\nsys: {}\n".format(
        end_time - start_time,
        end_res.ru_utime - start_res.ru_utime,
        end_res.ru_stime - start_res.ru_stime)


def trial_division(num: int):
    """
    Finds the smallest divisor
    Returns:
        smallest divisor if found
        0 if num is prime
    """
    while num % 2 == 0:
        return 2

    fac = 3
    while fac ** 2 <= num:
        if num % fac == 0:
            return fac
        else:
            fac += 2
    return 1


def print_factors():

    with open(sys.argv[1], 'r') as src:
        prime = src.readline()
        while prime != '':
            num = int(prime)
            res = trial_division(num)
            print("{}={}*{}".format(num, num//res, res))

            prime = src.readline()
