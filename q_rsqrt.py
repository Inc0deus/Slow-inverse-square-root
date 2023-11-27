import struct
from math import *
from time import *
from random import *


def f_bin(num):
    return int(format(struct.unpack('i', struct.pack('f', num))[0], '032b'), 2)

def bin_f(inp):
    return struct.unpack('f',struct.pack('i', inp))[0]

def q_rsqrt(inp):
    i: int
    x2: float
    y: float
    threehalfs = 1.5

    x2 = inp * 0.5
    y = inp
    i = f_bin(y)                # (the equivalent of) evil floating point bit level hacking
    i = 0x5f3759df - (i >> 1)   # what the fuck?
    y = bin_f(i)
    y = y * (threehalfs - (x2 * y * y))     # 1st iteration
    # y = y * (threehalfs - (x2 * y * y))   # 2nd iteration, this can be removed
    
    return y


N = 1000000
l = [uniform(0.0001, 10000) for i in range(N)]

t = time()
for n in l:
    k = q_rsqrt(n)
t1 = time() - t
print(t1)

t = time()
for n in l:
    k = 1/sqrt(n)
t2 = time() - t
print(t2)

print(t1/t2)
