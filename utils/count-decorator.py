import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{}:{} s'.format(func.__module__,func.__name__, end-start))
        # print('run time :{}s'.format( end-start))
        return r
    
    return wrapper

@timethis
def work(n=3):
    time.sleep(n)
    return 1

if __name__ == '__main__':
    # time.sleep(3)
    work(3)

    
