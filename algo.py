import numpy as np
import random

def SA(f,iteration, initial_value):
    
    # temperature
    def t(k):
        return 1/np.log(k+2)

    x = initial_value
    for i in range(iteration):
        y = list(np.random.normal(x,0.25*np.ones(10),(10,)))
        pk = np.exp(-max(0,(f(y)-f(x))/t(i)))
        p = np.random.random(1)[0]
        if p <= pk:
            x = y
    return x, f(x)


def FSA(f, iteration, initial_value):
    # temperature
    def t(k):
        return 1/(np.log(k+2)*(k+2))

    x = initial_value
    for i in range(iteration):
        y = list(np.random.normal(x,0.25*np.ones(10),(10,)))
        pk = 1/(1+max(0,(f(y)-f(x))/t(i)))
        p = np.random.random(1)[0]
        if p <= pk:
            x = y
    return x, f(x)

def SMC_SA(f, iteration, initial_value, N = 250): 
    # temperature
    def t(k):
        return 1/np.log(k+2)
    
    def piT(x,k):
        return np.exp(-f(x)/t(k))/np.exp(-f(x)/t(k-1))

    x = list(np.random.normal(initial_value,0.05*np.ones(10),(250,10,)))
    w = np.zeros(250)
    for k in range(1, iteration):
        for n in range(250):
            w[n] = piT(x[n],k)
        resample = random.choices(x,weights=w,k=250)
        x = resample
        for n in range(250):
            y = list(np.random.normal(x[n],0.25*np.ones(10),(10,)))
            pk = np.exp(-max(0,(f(y)-f(x[n]))/t(k)))
            p = np.random.random(1)[0]
            if p <= pk:
                x[n] = y
    
    sol = x[0]
    best = np.inf
    for i in range(250):
        if f(x[i]) < best:
            sol = x[i]
            best = f(x[i])

    return sol, best


def CSA(f, iteration, initial_value):
    # temperature
    def T(k):
        return 1/(np.log(k+2)*(k+2))
    
    def t(k):
        return 1/np.log(k+2)

    def piT(x,k):
        return np.exp(-f(x)/t(k))/np.exp(-f(x)/t(k-1))

    x = list(np.random.normal(initial_value,0.05*np.ones(10),(250,10,)))
    w = np.zeros(250)
    for k in range(1, iteration):
        for n in range(250):
            w[n] = piT(x[n],k)
        #print(w)
        #print(x)
        resample = random.choices(x,weights=w,k=250)
        x = resample
        for n in range(250):
            y = list(np.random.normal(x[n],0.25*np.ones(10),(10,)))
            pk = 1/(max(0,(f(y)-f(x[n]))/T(k))+1)
            p = np.random.random(1)[0]
            if p <= pk:
                x[n] = y
    
    sol = x[0]
    best = np.inf
    for i in range(250):
        if f(x[i]) < best:
            sol = x[i]
            best = f(x[i])

    return sol, best