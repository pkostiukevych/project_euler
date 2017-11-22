from math import floor, log, sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), floor(sqrt(n)-1)))

def prime_generator(stop=10001):
    n = 2
    counter = 1
    while counter <= stop:
        if is_prime(n):
            yield n
            counter += 1
        n += 1

def find_number(div_max=20):
    result = 1

    for prime in prime_generator():
        a = floor(log(div_max) / log(prime))
        result = result * int(pow(prime, a))

    return result
