from utils import exponentiate_modulate
from generate_keys import generate_keys


def encrypt(plaintext, pub_key):
    n, e = pub_key
    ciphertext = exponentiate_modulate(plaintext,e,n)

    return ciphertext

def decrypt(ciphertext, priv_key, n):
    plaintext = exponentiate_modulate(ciphertext, priv_key, n)

    return plaintext

def main():
    
    public_key, private_key = generate_keys()
    n, e = public_key
    print(f"Public key {public_key}")
    print(f"Private key {private_key}")
    plaintext = 13378

    ciphertext = encrypt(plaintext, public_key)
    decrypted_ciphertext = decrypt(ciphertext, private_key, n)
    print(f"Ciphertext: {ciphertext} \nPlaintext: {decrypted_ciphertext}")

    #encrypt("Asga sfgoijo asj  23o489j  sdnsvdsd oij09  lkjalhoi 12334994;;;;")

if __name__ == "__main__":
    main()