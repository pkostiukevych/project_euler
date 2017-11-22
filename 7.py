from math import sqrt, floor
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

def pe_7(stop=10001):
    item = None
    for item in prime_generator(stop):
        pass
    return item
