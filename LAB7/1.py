Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 # The proven prime
N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 # Number of points in the field
Acurve = 0
Bcurve = 7 # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
Gx = 550662630222773436695787188951685343262506034537775941755001
Gy = 326705100207588169780830851305070431844712733806592432759389
GPoint = (Gx,Gy) # This is our generator point. Trillions of dif ones possible

privKey = 0xB0EC65FFCB799873CBEA0AC274015B9526505DBBBED385155425F7337704883E
# inp = input("Enter Private Key to use: ")
# privKey = int(str(inp), 16)


def modinv(a,n=Pcurve): 
    lm, hm = 1,0
    low, high = a%n,n
    while low > 1:
        ratio = high/low
        nm, new = hm-lm*ratio, high-low*ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % n

def ECadd(a,b): 
    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],Pcurve)) % Pcurve
    x = (LamAdd*LamAdd-a[0]-b[0]) % Pcurve
    y = (LamAdd*(a[0]-x)-a[1]) % Pcurve
    return (x,y)

def ECdouble(a): 
    Lam = ((3*a[0]*a[0]+Acurve) * modinv((2*a[1]),Pcurve)) % Pcurve
    x = (Lam*Lam-2*a[0]) % Pcurve
    y = (Lam*(a[0]-x)-a[1]) % Pcurve
    return (x,y)

def EccMultiply(GenPoint,ScalarHex): 
    if ScalarHex == 0 or ScalarHex >= N: raise Exception("Invalid Scalar/Private Key")
    ScalarBin = str(bin(ScalarHex))[2:]
    Q=GenPoint
    for i in range (1, len(ScalarBin)):
        Q=ECdouble(Q)
        if ScalarBin[i] == "1":
            Q=ECadd(Q,GenPoint) 
    return (Q)

print("------- Public Key Generation -------") 

print("Using the private key:") 
print(privKey)
print("")
print("Using Point: ")
print(GPoint)
print("")
PublicKey = EccMultiply(GPoint,privKey)
print("public key:")
print(PublicKey) 
# print("the uncompressed public key (HEX):") 
# print("04" + "%064x" % PublicKey[0] + "%064x" % PublicKey[1]) 
# print("the official Public Key - compressed:") 
# if PublicKey[1] % 2 == 1: 
#     print("03"+str(hex(PublicKey[0])[2:-1]).zfill(64))
# else: 
#     print("02"+str(hex(PublicKey[0])[2:-1]).zfill(64))