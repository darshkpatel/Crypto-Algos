sharedPrime = 23    
sharedBase = 5      
 
aliceSecret = 6     
bobSecret = 15      
 
print( "Public Prime: " , sharedPrime )
print( "Public Base:  " , sharedBase )
 
A = (sharedBase**aliceSecret) % sharedPrime
print( "\nA Sends Publicaly  A = g^a mod p : " , A )
 
B = (sharedBase ** bobSecret) % sharedPrime
print("B Sends Publicaly B = g^b mod p : ", B )
 
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print( "Alice Shared Secret  s = B^a mod p: ", aliceSharedSecret )
 
bobSharedSecret = (A**bobSecret) % sharedPrime
print( "Bob Shared Secret s = A^b mod p: ", bobSharedSecret )