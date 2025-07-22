from utils.constants import MASK64, SIGMA
from utils.methods import rotl128
from .f_functions import f_function

def generate_subkeys(key: int) -> dict:

    KL = key
    KR = 0

    D1 = (KL ^ KR) >> 64
    D2 = (KL ^ KR) & MASK64
    D2 = D2 ^ f_function(D1, SIGMA[0])
    D1 = D1 ^ f_function(D2, SIGMA[1])
    D1 = D1 ^ (KL >> 64)
    D2 = D2 ^ (KL & MASK64)
    D2 = D2 ^ f_function(D1, SIGMA[2])
    D1 = D1 ^ f_function(D2, SIGMA[3])
    KA = (D1 << 64) | D2
    D1 = (KA ^ KR) >> 64
    D2 = (KA ^ KR) & MASK64
    D2 = D2 ^ f_function(D1, SIGMA[4])
    D1 = D1 ^ f_function(D2, SIGMA[5])
    #KB is not used in 128-bit
    KB = (D1 << 64) | D2 

    kw1 = rotl128(KL,0) >> 64
    kw2 = rotl128(KL,0) & MASK64
    k1  = rotl128(KA,0) >> 64
    k2  = rotl128(KA,0) & MASK64
    k3  = rotl128(KL,15) >> 64
    k4  = rotl128(KL,15) & MASK64
    k5  = rotl128(KA,15) >> 64
    k6  = rotl128(KA,15) & MASK64
    ke1 = rotl128(KA,30) >> 64
    ke2 = rotl128(KA,30) & MASK64
    k7  = rotl128(KL,45) >> 64
    k8  = rotl128(KL,45) & MASK64
    k9  = rotl128(KA,45) >> 64
    k10 = rotl128(KL,60) & MASK64
    k11 = rotl128(KA,60) >> 64
    k12 = rotl128(KA,60) & MASK64
    ke3 = rotl128(KL,77) >> 64
    ke4 = rotl128(KL,77) & MASK64
    k13 = rotl128(KL,94) >> 64
    k14 = rotl128(KL,94) & MASK64
    k15 = rotl128(KA,94) >> 64
    k16 = rotl128(KA,94) & MASK64
    k17 = rotl128(KL,111) >> 64
    k18 = rotl128(KL,111) & MASK64
    kw3 = rotl128(KA,111) >> 64
    kw4 = rotl128(KA,111) & MASK64

    return {
        "kw": [kw1, kw2, kw3, kw4],
        "k": [k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16, k17, k18],
        "ke": [ke1, ke2, ke3, ke4],
    }