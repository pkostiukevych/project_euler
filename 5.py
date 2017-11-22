import math

def gen_primes(lim):
    primes = [2]
    for i in range(3, lim, 2):
        is_prime= True
        j = 0
        while (primes[j] * primes[j] <= i):
            if i % primes[j] == 0:
                is_prime = False
                break
            j += 1

        if is_prime:
            primes.append(i)
    return primes

def find_number(div_max=20):
    primes = gen_primes(div_max)

    result = 1

    for _, prime in enumerate(primes):
        a = math.floor(math.log(div_max) / math.log(prime))
        result = result * int(pow(prime, a))

    return result
