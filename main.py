from utils import *
from generate_keys import generate_keys

def encrypt(plaintext, pub_key):
    n, e = pub_key
    return pow(plaintext, e, n)


def decrypt(ciphertext, priv_key):
    n, d = priv_key
    return pow(ciphertext, d, n)

def main():
    import time
    start = time.time()
    public_key, private_key = generate_keys()

    ciphertext = encrypt(333333333333333333333333333333333333333333333333333333333333333333333333333, public_key)
    decrypted_ciphertext = decrypt(ciphertext, private_key)
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted plaintext: {decrypted_ciphertext}")
    end = time.time()
    print(f"Time elapsed generating public and private key pair with primes size 512 bits, and encrypting data: {end-start}")    


    

if __name__ == "__main__":
    main()