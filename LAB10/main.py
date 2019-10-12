from random import getrandbits
from math import sqrt
from sys import exit
from gmpy2 import * 	
from gmpy2 import powmod
from Crypto.Hash import SHA1 as sha1		
from gmpy2 import xmpz
from random import randrange
from sys import stdin
N = 1024
L = 160
def inverse(z,a):
	if z > 0 and z < a and a > 0:
		i = a
		j = z
		y1 = 1
		y2 = 0
		while j > 0:
			q = i/j
			r = i-j*q
			y = y2 - y1*q
			i, j = j, r
			y2, y1 = y1, y
		if i == 1:
			return y2 % a
    
	raise Exception('Inverse Error')


def generate_p_q(L, N):
    g = N  
    n = (L - 1) // g
    b = (L - 1) % g
    while True:
       
        while True:
            s = xmpz(randrange(1, 2 ** (g)))
            a = sha1(to_binary(s)).hexdigest()
            zz = xmpz((s + 1) % (2 ** g))
            z = sha1(to_binary(zz)).hexdigest()
            U = int(a, 16) ^ int(z, 16)
            mask = 2 ** (N - 1) + 1
            q = U | mask
            if is_prime(q, 20):
                break

        i = 0 
        j = 2  
        while i < 4096:
            V = []
            for k in range(n + 1):
                arg = xmpz((s + j + k) % (2 ** g))
                zzv = sha1(to_binary(arg)).hexdigest()
                V.append(int(zzv, 16))
            W = 0
            for qq in range(0, n):
                W += V[qq] * 2 ** (160 * qq)
            W += (V[n] % 2 ** b) * 2 ** (160 * n)
            X = W + 2 ** (L - 1)
            c = X % (2 * q)
            p = X - c + 1  
            if p >= 2 ** (L - 1):
                if is_prime(p, 10):
                    return p, q
            i += 1
            j += n + 1


def generate_g(p, q):
    while True:
        h = randrange(2, p - 1)
        exp = xmpz((p - 1) // q)
        g = powmod(h, exp, p)
        if g > 1:
            break
    return g

def number_gen(p,q,g):
	c = getrandbits(N+64)
	k = (c % (q-1))+1
	try:
		k_ = inverse(k,q)
		return (k,k_) 
	except 'Inverse Error':
		return number_gen(p,q,g)
def sign((p,q,g), H, (x, y)):
	k,k_ = number_gen(p,q,g)
	r = powmod(g,k,p) % q
	z = long(H, 16)
	s = (k_*(z+x*r)) % q

	return (r, s)

def verify((p,q,g), H, y, (r,s)):
	if 0 < r and r < q and 0 < s and s < q:
		w = inverse(s, q)
		z = long(H, 16)
		u1 = (z*w) % q
		u2 = (r*w) % q
		v = ((powmod(g,u1,p) * powmod(y,u2,p)) % p) % q
		return v == r
	raise Exception('Verify Error')
		


def no_bits(p):
	return (len(bin(p))-2)

def range_(begin, stop):
   i = begin
   while i < stop:
       yield i
       i += 1

def group(list, n):
	return zip(* [list[i::n] for i in range(n)])

def gen_pair((p,q,g)):
	c = getrandbits(N+64)
        x = (c % (q-1)) + 1
        y = powmod(g,x,p)
        return (x,y)
def generate_params(L, N):
    p, q = generate_p_q(L, N)
    g = generate_g(p, q)
    return p, q, g
if __name__=='__main__':

	p,q,g = generate_params(L,N)



	token = raw_input()
	if token == 'genkey':
                n = long(raw_input()[2:])
                while n > 0:
                        (x,y) = gen_pair((p,q,g))
                        print "x=" + str(x)
                        print "y=" + str(y)
                        n -= 1

	elif token == 'sign':
		x = long(raw_input()[2:])
		y = long(raw_input()[2:])
		Ds = [l[2:-1] for l in stdin]
		signs = [sign((p,q,g), d, (x,y)) for d in Ds]
		for (r,s) in signs:
			print 'r='+str(r)
			print 's='+str(s)

	elif token == 'verify':
		y = long(raw_input()[2:])
		tuples = group([l[2:-1] for l in stdin], 3)  # tuples (D, r, s)
		verifies = [verify((p,q,g), t[0], y, (long(t[1]), long(t[2]))) for t in tuples]
                for v in verifies:
                        if v:
                                print 'signature_valid'
                        else:
                                print 'signature_invalid'