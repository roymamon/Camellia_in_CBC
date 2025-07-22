from utils.constants import MASK8
from camellia.sbox import SBOX1, SBOX2, SBOX3, SBOX4

def f_function(F_IN: int, KE: int) -> int:

    #var x as 64-bit unsigned integer
    x  = F_IN ^ KE
    #var t1, t2, t3, t4, t5, t6, t7, t8 as 8-bit unsigned integer
    #var y1, y2, y3, y4, y5, y6, y7, y8 as 8-bit unsigned integer
    t1 =  x >> 56
    t2 = (x >> 48) & MASK8
    t3 = (x >> 40) & MASK8
    t4 = (x >> 32) & MASK8
    t5 = (x >> 24) & MASK8
    t6 = (x >> 16) & MASK8
    t7 = (x >>  8) & MASK8
    t8 =  x & MASK8
    t1 = SBOX1[t1]
    t2 = SBOX2[t2]
    t3 = SBOX3[t3]
    t4 = SBOX4[t4]
    t5 = SBOX2[t5]
    t6 = SBOX3[t6]
    t7 = SBOX4[t7]
    t8 = SBOX1[t8]
    y1 = t1 ^ t3 ^ t4 ^ t6 ^ t7 ^ t8
    y2 = t1 ^ t2 ^ t4 ^ t5 ^ t7 ^ t8
    y3 = t1 ^ t2 ^ t3 ^ t5 ^ t6 ^ t8
    y4 = t2 ^ t3 ^ t4 ^ t5 ^ t6 ^ t7
    y5 = t1 ^ t2 ^ t6 ^ t7 ^ t8
    y6 = t2 ^ t3 ^ t5 ^ t7 ^ t8
    y7 = t3 ^ t4 ^ t5 ^ t6 ^ t8
    y8 = t1 ^ t4 ^ t5 ^ t6 ^ t7

    F_OUT = (y1 << 56) | (y2 << 48) | (y3 << 40) | (y4 << 32)| (y5 << 24) | (y6 << 16) | (y7 <<  8) | y8
    
    return F_OUT