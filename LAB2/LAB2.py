#http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
#DES - KEY GENERATION

from sys import exit
from helpers import *
from tables import *

seed=list(map(int,input("Enter Key Seed: ")))
#seed=list(map(int,"11110000110011001010101011110101010101100110011110001111"))

# parity_drop_PC1 = apply_permutation(seed,PC_1)
# print(parity_drop_PC1)

#########################################################################################
left_seed = left_half(seed)
right_seed = right_half(seed)


for ROUND in range(1,17):
    if(ROUND in [1,2,9,16]):
        left_seed = left_shift(1,left_seed)
        right_seed = left_shift(1,right_seed)
    else:
        left_seed = left_shift(2,left_seed)
        right_seed = left_shift(2,right_seed)
    combined = left_seed+right_seed
    print("\nKEY " , ROUND, ": " , ''.join(list(map(str, apply_permutation(combined, PC_2)))))