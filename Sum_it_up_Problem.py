import numpy as np


def sum_it_up(i):
    if type(i) is int:
        count = 0
        for j in range(i+1):
            count += j
        return count
    else:
        return 0


def sum_it_up_2(i):
    if type(i) is int:
        return np.sum(np.arange(i+1))
    else:
        return 0


print(sum_it_up(2000))  #0+1+2+3+4+5
print(sum_it_up_2(2000))