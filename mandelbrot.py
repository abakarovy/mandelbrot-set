from math import log, log2

max_iters = 40

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iters:
        try:
            z = (z*z) + c
            
        except:
            ZeroDivisionError
        n+=1

    if n==max_iters:
        return max_iters
    return n + 1 - log(log2(abs(z)))