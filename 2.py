def even_fib_generator(lim):
    a, b = 1, 1
    while a < lim:
        if not a % 2:
            yield a
        a, b = b, a + b

def pe_2(lim=4000000):
    return sum(even_fib_generator(lim))
