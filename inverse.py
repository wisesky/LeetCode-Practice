import numpy as np
import matplotlib.pyplot as plt
class Sample:
    def inverse(self, sampleSize):
        # F(x) = 1 - e**(-x)  反函数F-(x) = -In(1-x)
        def getInverseFunc(sampleSize):
            return -np.log(1-np.random.uniform(0,1,sampleSize))
        es = getInverseFunc(sampleSize)
        plt.hist(es, np.linspace(0,5,50))
        plt.show()

if __name__ == "__main__":
    sampleSize = 1000000
    s = Sample()
    s.inverse(sampleSize)