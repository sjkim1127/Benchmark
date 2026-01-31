CC = clang
CFLAGS = -O3 -Wall

all: main

main: main.c matmul_neon.s
	$(CC) $(CFLAGS) -o main main.c matmul_neon.s

clean:
	rm -f main
