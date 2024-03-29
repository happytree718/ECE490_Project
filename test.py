import numpy as np

def testProgram(algo_func, obj_func, iteration, initial_val, runs=50):
    val = np.zeros(runs)
    for i in range(runs):
        _,best_val = algo_func(obj_func,iteration,initial_val)
        val[i] = best_val
    # print(val)
    return np.mean(val),np.std(val)    
