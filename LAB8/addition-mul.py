Pcurve = 11 # The proven prime


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
    ScalarBin = str(bin(ScalarHex))[2:]
    Q=GenPoint
    for i in range (1, len(ScalarBin)):
        Q=ECdouble(Q)
        if ScalarBin[i] == "1":
            Q=ECadd(Q,GenPoint) 
    return (Q)

print("ECC Point Addition and Multiplication - 18BCI0211")
print("1. Addition \n2. Multiplication\n")
choice = input("Choice: ")


print("y^2 = x^3 + Acurve * x + Bcurve (mod Pcurve)")

Acurve = int(input("Enter Acurve: "))
Bcurve = int(input("Enter Bcurve: "))
Pcurve = int(input("Enter Pcurve: "))

if choice == 1 or choice =="1":
    p1 = eval(input("Enter P1 (x,y):"))
    p2 = eval(input("Enter P2 (x,y):"))
    print("ECC Point Addition\n")
    print("P1 + P2 = ", ECadd(p1, p2))
if choice == 2 or choice =="2":
    p1 = eval(input("Enter P1 (x,y):"))
    n = int(input("Enter Multiplication Scalar N:"))
    print("ECC Point Multiplication\n")
    print("N * P1 = ", EccMultiply(p1, n))
    


