import math


def pe_3(num=600851475143):

    max_divisor = 0
    counter = 2
    while (counter * counter <= num):
        if num % counter == 0:
            num = num / counter
            max_divisor = counter
        else:
            counter += 1

    return max(max_divisor, num)
        

    

            
