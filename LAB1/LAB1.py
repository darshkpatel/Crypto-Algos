from sys import exit
from helpers import *

ip = [2,6,3,1,4,8,5,7]
ip_inv = [4,1,3,5,7,2,8,6]
p10 = [3,5,2,7,4,10,1,9,8,6]
p8 = [6,3,7,4,8,5,1,9]

#plaintext=list(map(int,input("Enter 8-bit plaintext: ")))
#key=list(map(int,input("Enter 10-bit key: ")))

plaintext = [1, 0, 1, 0, 0, 0, 1, 1] # 10100011
key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0] # 1010000010

if len(plaintext)!=8 or len(key)!=10:
	print("Invalid Input")
	exit(1)

print("Plaintext", ''.join(list(map(str, plaintext))))
print("key", ''.join(list(map(str, key))))

######################################################################
print("Key Generation")
p10_of_key=apply_permutation(key,p10)

L_left_shift1=left_shift(1,left_half(p10_of_key))
R_left_shift1=left_shift(1,right_half(p10_of_key))

key1=apply_permutation(L_left_shift1+R_left_shift1,p8)
print("Key 1: "+ str(key1))

L_left_shift2=left_shift(2,L_left_shift1)
R_left_shift2=left_shift(2,R_left_shift1)

key2=apply_permutation(L_left_shift2+R_left_shift2,p8)
print("Key 2: "+str(key2))
print("")

######################################################################

print("---Encryption---")
initial_permutation = apply_permutation(plaintext, ip)
print("Initial Permutation: ", initial_permutation)

print("Round Function With Key 1:")
round1_output = round_function_and_swap(initial_permutation, key1)
swapped = swap(round1_output)
print("\nRound Function With Key 2:")
round2_output = round_function_and_swap(swapped, key2)

cipher_text = initial_permutation_inv = apply_permutation(round2_output, ip_inv)
print("\nCipher Text :", cipher_text)

######################################################################

print("\n\n---Decryption---")
print("Decrypting Same Cypher Text: ", cipher_text)

initial_permutation = apply_permutation(cipher_text, ip)
print("Initial Permutation: ", initial_permutation)

print("\nRound Function With Key 2:")
round2_output = round_function_and_swap(initial_permutation, key2)
swapped = swap(round2_output)
print("\nRound Function With Key 1:")
round1_output = round_function_and_swap(swapped, key1)

plain_text = initial_permutation_inv = apply_permutation(round1_output, ip_inv)
string_plain = ''.join(list(map(str, plain_text)))

print("Decrypted Plain Text: " , plain_text)


