import collections

def main():
    try:
        with open("../../data/input.txt", "r") as f:
            content = f.read()
            # Split by whitespace
            words = content.split()
            counts = collections.Counter(words)
            print(f"Unique words: {len(counts)}")
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
