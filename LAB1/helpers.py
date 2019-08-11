def left_shift(pos, arr):
	left =  arr[pos:]
	right = arr[:pos]
	return left+right

def apply_permutation(arr,key):
	final=[]
	for index in key:
		final.append(arr[index-1])
	return final

def left_half(arr):
    return arr[:len(arr)//2]

def right_half(arr):
    return arr[len(arr)//2:]

def xor(arr1, arr2):
    final = []
    for arr1_num, arr2_num in zip(arr1, arr2):
        final.append(((int(arr1_num) + int(arr2_num)) % 2)) 
    return final

def find_inside_sBox(arr, matrix):
	row = int(str(arr[0]) + str(arr[3]), 2)
	col = int(str(arr[1]) + str(arr[2]), 2)
	binary = '{0:02b}'.format(matrix[row][col])
	return list(map(int,binary))

def round_function_and_swap(arr,key):
	ep=[4,1,2,3,2,3,4,1]
	s0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
	s1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
	p4 = [2,4,3,1]

	left = left_half(arr)
	right = right_half(arr)
	ep_of_arr = apply_permutation(right, ep)
	print("	EP Output: ", ep_of_arr)
	xored_bits = xor(ep_of_arr, key)
	final_4bits = find_inside_sBox( left_half(xored_bits), s0) + find_inside_sBox(right_half(xored_bits), s1)
	print("from s box: ", final_4bits)
	bits = apply_permutation(final_4bits, p4)
	print("from s box + Xor: ", bits)
	xored_P4bits =  xor(bits, left)
	print("	Xored P4: ", xored_P4bits)
	joined = xored_P4bits+right
	return joined
def swap(arr):
	return right_half(arr)+left_half(arr)