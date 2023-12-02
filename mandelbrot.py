max_iters = 20

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iters:
        try:
            z = (z**2) + c
            
        except:
            ZeroDivisionError
        n+=1
    return n