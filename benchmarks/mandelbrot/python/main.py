import sys

WIDTH = 2048
HEIGHT = 2048
MAX_ITER = 255

def main():
    # Pre-allocate list? Or bytearray?
    # bytearray is mutable and strictly typed (0-255), closer to C.
    buffer = bytearray(WIDTH * HEIGHT)
    
    min_x = -2.0
    max_x = 0.47
    min_y = -1.12
    max_y = 1.12
    
    scalex = (max_x - min_x) / WIDTH
    scaley = (max_y - min_y) / HEIGHT
    
    # Pre-calculate cy and cx to save some time?
    # Let's keep loop structure identical to others.
    
    for y in range(HEIGHT):
        cy = min_y + y * scaley
        offset = y * WIDTH
        for x in range(WIDTH):
            cx = min_x + x * scalex
            
            zx = 0.0
            zy = 0.0
            zx2 = 0.0
            zy2 = 0.0
            
            iter = 0
            while iter < MAX_ITER and (zx2 + zy2) < 4.0:
                zy = 2.0 * zx * zy + cy
                zx = zx2 - zy2 + cx
                zx2 = zx * zx
                zy2 = zy * zy
                iter += 1
            
            buffer[offset + x] = iter

    total_sum = sum(buffer)
    print(f"Done. Sum: {total_sum}")

if __name__ == "__main__":
    main()
