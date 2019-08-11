#http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
#DES - KEY GENERATION

from sys import exit
from helpers import *
from tables import *
from f_func import *

#seed=list(map(int,input("Enter Key Seed: ")))
seed=list(map(int,"11110000110011001010101011110101010101100110011110001111"))

# parity_drop_PC1 = apply_permutation(seed,PC_1)
# print(parity_drop_PC1)

#########################################################################################
left_seed = left_half(seed)
right_seed = right_half(seed)

keys = []
for ROUND in range(1,17):
    if(ROUND in [1,2,9,16]):
        left_seed = left_shift(1,left_seed)
        right_seed = left_shift(1,right_seed)
    else:
        left_seed = left_shift(2,left_seed)
        right_seed = left_shift(2,right_seed)
    combined = left_seed+right_seed
    keys.append(''.join(list(map(str, apply_permutation(combined, PC_2)))))




#plaintext = input("Enter Plaintext: ")
plaintext = "0123456789ABCDEF"
plaintext = bin(int(plaintext, 16))[2:].zfill(64)
print("\n --- Encryption ---")
print("Entered Plaintext:", hex(int(plaintext,2)))
print("M: ", plaintext)
plaintext = list(map(int, plaintext))





def encrypt_des(arr_64, keys):



    # Perform initial permutation on block
    p = ""
    for number in ip:
        p += arr_64[number-1]

    print("IP: ", p)
    # Split block into two halves
    ln = p[:32]
    rn = p[32:]

    # 16 rounds of encryption, rotating and XORing each half after each round
    for i in range(16):
        temp = rn
        rn = bin(int(ln, 2) ^ int(f_func(rn, keys[i]), 2))[2:].zfill(32)
        ln = temp

    # Combine left and right halves and perform final permutation
    combined = rn + ln
    out = ""
    for number in fp:
        out += combined[number-1]

    print("IP Inv: ", out)


    return out




def decrypt_des(arr_64, keys):


    p = ""
    for number in ip:
        p+= arr_64[number-1]
    # print("IP: ", p)

    ln = p[:32]
    rn = p[32:]


    for i in range(15, -1, -1):
        temp = rn
        rn = bin(int(ln, 2) ^ int(f_func(rn, keys[i]), 2))[2:].zfill(32)
        ln = temp

    combined = rn+ln

    out = ""
    for number in fp:
        out += combined[number-1]

    # print("FP: ", out)
    return out
        






output = encrypt_des(''.join(list(map(str,plaintext))), keys)
print("CipherText In Hex: ", hex(int(output,2)))

print("\n --- Decryption ---")
print("Inputed CipherText: ", hex(int(output,2)))
dec_plaintext = decrypt_des(output, keys)
print("Decrypted Plaintext: ", dec_plaintext)
print("Decrypted Plaintext in Hex: ", hex(int(dec_plaintext,2)))