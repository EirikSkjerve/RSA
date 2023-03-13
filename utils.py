def exponentiate_modulate(base, power, mod):
    if power == 0:
        return 1
    
    if power == 1:
        return base%mod
    
    temp = base*base%mod
    for _ in range(2, power):
        temp = (temp*base)%mod

    return temp

def convert_string_to_integer_blocks(string, blocksize = 10)->list:
    binary = ''.join(bin(ord(x))[2:] for x in string)
    blocks = [binary[i:i+blocksize].zfill(blocksize) for i in range(0,len(binary), blocksize)]
    messages_int = [int(b,2) for b in blocks]
    return messages_int


# ascii
def convert_ascii_to_integers(input, block_size=10):
    output = [ord(i) for i in input]
    return output

#print(convert_ascii_to_integers("Hei", block_size=10))