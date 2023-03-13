import random as random
import math
#from primePy import primes
from primality import primality

def generate_keys()->tuple:
    p, q = generate_primes()
    
    # public keygen
    n = p*q
    m = (p-1)*(q-1)
    e = find_invertible_number(m)

    public_key = (n,e)

    # private keygen
    d = invert_number(e, m)
    private_key = n, d
    
    return (public_key, private_key)

def find_invertible_number(m)->int:
    #print("Finding an invertible number...")
    for p in range(3, m):

        if math.gcd(p,m) == 1:
            return p
        
def invert_number(e, m)->int:
    #print("Finding inverse of e...")

    return pow(e, -1, m)



def generate_primes()->tuple:

    #fast approach
    p = 0
    #print("Generating p...")
    while True:
        random_number = random.randrange(2**512 + 1, 2**513 + 1,2)
    
        if primality.isprime(random_number):
            p = random_number
            break
        random_number += 2
        
    q = 0
    #print("Generating q...")
    while True:
        random_number = random.randrange(2**512 + 1, 2**513 + 1,2)
    
        if primality.isprime(random_number):
            q = random_number
            break
        random_number += 2
    return p, q