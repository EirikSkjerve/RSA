def exponentiate_modulate(base, power, mod):
    if power == 0:
        return 1
    
    if power == 1:
        return base%mod
    
    temp = base*base%mod
    for _ in range(2, power):
        temp = (temp*base)%mod

    return temp
