CC = clang
CFLAGS = -O3 -Wall

all: main

main: main.c fib.s
	$(CC) $(CFLAGS) -o main main.c fib.s

clean:
	rm -f main
