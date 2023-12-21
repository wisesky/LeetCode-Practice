#! python3
# -*- encoding: utf-8 -*-
'''
@File   : timethis.py
@Time   : 2021/12/27 18:22:02
@Author : Franklin Chen
@Contact: wisesky1988@gmail.com
@Licence: MIT License
'''
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        r = func(*args, **kwargs)
        end = time.process_time()
        print(f"{func.__module__}.{func.__name__} process time : {end-start} s")
        # print(f" process time : {end-start} s")
        return r
    return wrapper

@timethis
def countdown(n):
    r = 1
    while n > 0:
        r *= n
        n -= 1

if __name__=='__main__':
    countdown(10000)