
import os

langs = ["swift", "java", "zig"]
categories = ["sieve", "fibonacci", "binary_tree", "word_count", "matrix_mul", "concurrency", "mandelbrot"]

makefiles = {
    "swift": """CC = swiftc
CFLAGS = -O

all: main

main: main.swift
\t$(CC) $(CFLAGS) main.swift -o main

clean:
\trm -f main
""",
    "java": """CC = javac

all: Main.class

Main.class: Main.java
\t$(CC) Main.java

clean:
\trm -f *.class
""",
    "zig": """CC = zig

all: main

main: main.zig
\t$(CC) build-exe main.zig -O ReleaseFast --name main

clean:
\trm -f main main.o
"""
}

for cat in categories:
    for lang in langs:
        path = os.path.join("benchmarks", cat, lang, "Makefile")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(makefiles[lang])
        print(f"Created {path}")
