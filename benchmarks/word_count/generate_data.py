import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
         "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla"]

# Generate ~50MB file
target_size = 50 * 1024 * 1024
current_size = 0

with open("../data/input.txt", "w") as f:
    while current_size < target_size:
        chunk = " ".join(random.choices(words, k=1000)) + " "
        f.write(chunk)
        current_size += len(chunk)

print("Generated input.txt")
