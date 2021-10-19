import time
from functools import wraps

def timethis(level='INFO'): 
    def decorate(func): 
        @wraps(func) 
        def wrapper(*args, **kargs): 
            start = time.time() 
            r = func(*args, **kargs) 
            end = time.time() 
            print(level, '  time take : %f s' % (end-start)) 
            return r 
        return wrapper 
    return decorate 

@timethis('class') 
class spam: 
    @timethis('instance') 
    def instance_method(self, n): 
        print(self, n) 
        while n>0: 
            n -=1 

s = spam()

s.instance_method(1000)