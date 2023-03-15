import numpy as np
from algo import SA, FSA, SMC_SA, CSA
from test import testProgram

def fa(x):
    return sum(5*(x[i+1]-x[i]**2)**2 + (1-x[i])**2 for i in range(9))

def fb(x):
    return 10 + sum(x[i]**2 - np.cos(2*np.pi*x[i]) for i in range(10))

if __name__ == "__main__":
    N = 500
    func = fa
    algo = CSA

    x0 = np.zeros(10)
    x1 = np.ones(10)
    initial_x = x0

    mean,std = testProgram(algo,func,N,initial_x)
    print(mean,std)