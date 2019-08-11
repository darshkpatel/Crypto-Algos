from aes_helpers import *
input_key = input("Enter 128 bit key in HEX: ")
# input_key = "5468617473206D79204B756E67204675"
input_key = input_key.rstrip().replace(" ","")
words = split_string(8,input_key)
words = [split_string(2,word) for word in words]
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
        generated_word = xor_str(words[i-4],words[i-1])
        words.append(int_to_hex(generated_word))
    else:
        # print(i-4,"XOR G( ", i-1,")")
        generated_word = xor_str(words[i-4],key_expansion_core(words[i-1],key_round+1))
        words.append(int_to_hex(generated_word))
        key_round+=1
    # print(words[i])

new = []
for x in range(len(words)):
    if(x==0 or x%4==0):
        count = 0
        # print(new)
        if len(new):
            final = [''.join(x) for x in new]
            final = ''.join(final)
            spaced = split_string(2, final)
            final = ' '.join(spaced)
            print("Key:",(x//4) - 1,"-",final)
        new = []

    new.append(words[x])