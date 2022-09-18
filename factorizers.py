#!/usr/bin/python3
import sys

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


def trial_division(n: int) -> int:
    """
    Finds the smallest divisor of n
    Returns:
        smallest divisor if found
        0 if n is prime
    """
    while n % 2 == 0:
        return 2

    fac  = 3
    while fac * fac <= n:
        if n % fac == 0:
            return fac
        else:
            fac  += 2
    # if n is prime
    return 1


def print_factors():

    with open(sys.argv[1], 'r') as src:
        prime = src.readline()
        while prime  != '':
            num = int(prime)
            res = trial_division(num)
            print("{}={}*{}".format(num, num//res, res))

            prime  = src.readline()
