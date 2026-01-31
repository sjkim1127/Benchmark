
import numpy as np
import time

def mandelbrot(w, h, max_iter):
    y, x = np.ogrid[-1.5:0.5:h*1j, -2.0:0.5:w*1j]
    c = x + y*1j
    z = c
    divtime = np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 4
        div_now = diverge & (divtime == 0)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

def main():
    w, h = 2048, 2048
    max_iter = 255
    
    # Measuring vectorized operation
    mandelbrot(w, h, max_iter)
    print("Done")

if __name__ == "__main__":
    main()
