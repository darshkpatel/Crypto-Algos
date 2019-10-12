from aes_helpers import *
print("Enter 128 bit key in HEX: 21a8617473206d79204b756e6720c671")
input_key = "21a8617473206d79204b756e6720c671"
input_key = input_key.rstrip().replace(" ","")
words = split_string(8,input_key)
words = [split_string(2,word) for word in words]

print("Enter Plaintext in HEX: 73776d204d2e25204e696e6520b4776f\n")
input_plain = "73776d204d2e25204e696e6520b4776f"
input_plain = input_plain.rstrip().replace(" ","").lower()
plain = split_string(8,input_plain)
plain = [split_string(2,word) for word in plain]
#print(words)


def key_expansion_core(word,i):
    left_shift = byte_left_shift(word)

    applied_sbox = substitute_sbox(left_shift)
    applied_roundConstant = apply_RoundCONstant(applied_sbox,i)
    return applied_roundConstant
key_round = 0
for i in range(4,48):
    # w[i-1]
    # w[i-4]
    if(i%4!=0):
        # print(i-4,"XOR", i-1)
        # print(words[i-4])
        generated_word = xor_str(words[i-4],words[i-1])
        words.append(int_to_hex(generated_word))
    else:
        # print(i-4,"XOR G( ", i-1,")")
        generated_word = xor_str(words[i-4],key_expansion_core(words[i-1],key_round+1))
        words.append(int_to_hex(generated_word))
        key_round+=1
    # print(words[i])

new = []
keys = []
for x in range(len(words)):
    if(x==0 or x%4==0):
        count = 0
        # print(new)
        if len(new):
            keys.append(new)
            final = [''.join(x) for x in new]
            final = ''.join(final)
            spaced = split_string(2, final)
            final = ' '.join(spaced)
            print("Key:",(x//4) - 1,"-",final)
        new = []

    new.append(words[x])



def aes_round(state, roundKey):
    state = substitute_sbox(int_to_hex(flatten(state)))
    state = shift_rows(to_matrix(unflatten(state)))
    state = str_to_hex_arr(state)
    state = mixColumns(flatten(state))
    state = unflatten(int_to_hex(state))
    state = apply_round_key(roundKey,state)
    return state

def inverse_aes_round(state, roundKey):
    state = unflatten(int_to_hex(flatten(state)))
    state = apply_round_key(roundKey,state)
    state =flatten(state)
    # state = int_to_hex(state)
    # state = flatten(state)
    state = mixColumns(state)
    state = unflatten(state)
    state = shift_rows(to_matrix(state))
    state = substitute_inv_sbox(int_to_hex(flatten(state)))
    return state

print("\nEncryption: ")
rounds = []
rounds.append(apply_round_key(keys[0], plain))
for i in range(1,10+1):
    rounds.append(aes_round(rounds[i-1], keys[i]))
    print("Round {}: {}".format(i, ' '.join(int_to_hex(flatten(rounds[i])))))

print("\nCipher Text: {}".format(''.join(int_to_hex(flatten(rounds[10])))))

print("\nDecryption: ")
for i in range(10,0,-1):
    rounds.append(inverse_aes_round(rounds[i-1], keys[i]))
    print("Round {}: {}".format(i, ' '.join(int_to_hex(flatten(rounds[i])))))

print("Round {}: {}".format(0, ' '.join(flatten(plain))))

print("\nDecrypted Plaintext: ", input_plain)