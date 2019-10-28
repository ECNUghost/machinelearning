import numpy as np
import time

def sum_trad():
    start = time.time()
    x = range(10000000)
    y = range(10000000)
    z = []
    for i in range(len(x)):
        z.append(x[i] + y[i])
    return time.time() - start

def sum_numpy():
    start = time.time()
    x = np.arange(100000)
    y = np.arange(100000)
    z = x + y
    return time.time() - start

print('time_sum:',sum_trad(),'time_sum_numpy',sum_numpy())