from fast_exponentiation import exponentiate_modulate
from primePy import primes
import random as random
import math

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
    prime_list_a = primes.between(1000, 2000)
    rand_a = random.randint(0, len(prime_list_a))
    
    p = prime_list_a[rand_a]

    prime_list_b = primes.between(2001, 3000)
    rand_b = random.randint(0, len(prime_list_b))
    
    q = prime_list_b[rand_b]

    return p,q


def encrypt(plaintext, pub_key):
    n, e = pub_key
    ciphertext = exponentiate_modulate(plaintext,e,n)

    return ciphertext

def decrypt(ciphertext, priv_key, n):
    plaintext = exponentiate_modulate(ciphertext, priv_key, n)

    return plaintext

if __name__ == "__main__":
    
    public_key, private_key = generate_keys()
    n, e = public_key
    print(f"Public key {public_key}")
    print(f"Private key {private_key}")
    plaintext = 1110

    ciphertext = encrypt(plaintext, public_key)
    decrypted_ciphertext = decrypt(ciphertext, private_key, n)
    print(f"Ciphertext: {ciphertext} \nPlaintext: {decrypted_ciphertext}")

    #encrypt("Asga sfgoijo asj  23o489j  sdnsvdsd oij09  lkjalhoi 12334994;;;;")