def pe_1(lim=1000):
    return sum([n for n in range(lim) if n % 3 == 0 or n % 5 == 0])
