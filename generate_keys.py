import random as random
import math
from primePy import primes

def generate_keys()->tuple:
    p, q = generate_primes()
    
    # public keygen
    n = p*q
    m = (p-1)*(q-1)
    e = find_invertible_number(m)

    public_key = (n,e)

    # private keygen
    d = invert_number(e, m)
    private_key = d
    
    return (public_key, private_key)

def find_invertible_number(m)->int:
    for p in range(3, m):

        if math.gcd(p,m) == 1:
            return p
        
def invert_number(e, m)->int:
    for i in range(m):
        if (e*i)%m == 1:
            return i
    return None


def generate_primes()->tuple:
    random.seed(13425123)
    prime_list_a = primes.between(10000, 20000)
    rand_a = random.randint(0, len(prime_list_a))
    
    p = prime_list_a[rand_a]

    prime_list_b = primes.between(20001, 30000)
    rand_b = random.randint(0, len(prime_list_b))
    
    q = prime_list_b[rand_b]

    return p,q
