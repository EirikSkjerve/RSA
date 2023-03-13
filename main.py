from generate_keys import generate_keys
import numpy as np

def encrypt(plaintext, pub_key):
    n, e = pub_key
    return pow(plaintext, e, n)


def decrypt(ciphertext, priv_key):
    n, d = priv_key

    return pow(ciphertext, d, n)
    

if __name__ == "__main__":
    #main()

    # encrypting a file

    with open("RSA/testfile.txt", "rb") as f:
        bin_data = f.read()

    binary_string = ''.join(['{:08b}'.format(byte) for byte in bin_data])

    # Split binary string into blocks of 100 bits
    block_size = 100
    plaintext_blocks = [int(binary_string[i:i+block_size], 2) for i in range(0, len(binary_string), block_size)]

    print(plaintext_blocks)

    public_key, private_key = generate_keys()
    ciphertext = [encrypt(c, public_key) for c in plaintext_blocks]
    print(ciphertext)

    decrypted_ciphertext = [decrypt(d, private_key) for d in ciphertext]
    
    # Convert base 10 integers to binary strings
    binary_blocks = ['{0:b}'.format(n) for n in ciphertext]

    # Pad each binary string to have length 100
    binary_blocks_padded = [s.zfill(100) for s in binary_blocks]

    # Concatenate binary strings into single binary string
    binary_string = ''.join(binary_blocks_padded)

    



    
    
