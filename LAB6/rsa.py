from math import gcd
import random

def int_to_hex(st):
    return list(map(lambda x:format(x, '02x'), st))

def is_prime_no(num):
	for i in range(2,int(num/2)+1):
		if(num%i==0):
			return 0
	return 1

def calc_E(p,q,ph):
	list1 = []
	for e in range(2,ph):
		if gcd(e,ph) == 1:
			list1.append(e)
	return list1
	
def calc_D(ph,e):
	for d in range(1,ph):
		if (d*e)%ph is 1:
			return d
			
def character_algo(pt,e,n,d):
	enc = []
	dec = []
	for i in pt:
		c = (ord(i)**e)%n
		enc.append(c)
	out_enc = int_to_hex(enc)	
	print("Encrpyted Plaintext: ",' '.join(out_enc))
	#print(enc)
	for j in enc:
		m = (j**d)%n
		dec.append(chr(m))
	str1 = ''.join(dec)
	print("Decrpyted Ciphertext: ",str1)
	# print(str1)
			
	
	
# def algo(data,e,n,d):
# 	c = (data**e)%n
# 	outc = int_to_hex(c)
# 	print("Encrpyted data : "+str(c))
# 	print("--------------------------------------")
# 	dec = (c**d)%n
# 	print("Decrypted data :"+str(dec))

def driver():
	p = int(input("Enter the first prime :"))
	while is_prime_no(p)==0:
		p = int(input("Invalid Number, Please enter the first PRIME number:"))
	q = int(input("Enter the second prime :"))
	while is_prime_no(q)==0:
		q = int(input("Invalid Number, Please enter the second PRIME number:"))
	n=p*q
	ph = (p-1)*(q-1)
	list1 = calc_E(p,q,ph)
	print("--------------------------------------")
	print("Number of Primes Generated: {} for e".format(len(list1)))
	print("Selecting Random Prime Number")
	e = random.choice(list1)
	print("Value of 'e' Selected:  "+ str(e))
	d = calc_D(ph,e)
	print("Calculated value of 'd': " +str(d))
	print("--------------------------------------")
	print("Public key: n="+str(n)+", e="+str(e))
	print("Private key: n="+str(n)+", d="+str(d))
	print("--------------------------------------")
	pt = input('Input Plaintext to Encrypt: ')
	if pt.isdigit():
		pt = int(pt)
		algo(pt,e,n,d)
	else:
		character_algo(pt,e,n,d)

driver()