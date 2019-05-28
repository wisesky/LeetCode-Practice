import numpy as np
import random as rd
import matplotlib.pyplot as plt
import math
import seaborn as sns
def test(sampleSize, s):
    #f = 
    d = []
    x = s
    for i in range(sampleSize):
        y = np.random.normal(x, 1)
        #y = np.random.rand()
        xx = func(x)
        yy = func(y)
        acpt = min(1, yy/xx)
        r = rd.random()
        if r < acpt:
            x = y
        d.append(x)


    print(d)
    #return d
    sns.distplot(d)
    plt.show()

def func(x):
    return 0.3 * math.exp((-0.2) * x * x) + 0.7 * math.exp((-0.2) * pow(x-10, 2))
    #return np.sqrt(1/(2*np.pi))*np.power(np.e,(-0.5)*(x-10)**2)

if __name__ == "__main__":
    test(5000,0)
