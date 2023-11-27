import struct

def f_bin(x):    # ~> * ( long * ) &x
    return int(format(struct.unpack('i', struct.pack('f', x))[0], '032b'), 2)

def bin_f(x):    # ~> * ( float * ) &x
    return struct.unpack('f',struct.pack('i', x))[0]

def q_rsqrt(number):
    i: int
    x2: float
    y: float
    threehalfs = 1.5

    x2 = number * 0.5
    y = number
    i = f_bin(y)                # (the equivalent of) evil floating point bit level hacking
    i = 0x5f3759df - (i >> 1)   # what the fuck?
    y = bin_f(i)
    y = y * (threehalfs - (x2 * y * y))     # 1st iteration
    # y = y * (threehalfs - (x2 * y * y))   # 2nd iteration, this can be removed
    
    return y
