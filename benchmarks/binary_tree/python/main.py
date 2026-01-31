import sys

# Increase recursion limit just in case, though 20 is fine
sys.setrecursionlimit(2000)

class Node:
    __slots__ = ['left', 'right'] # Optimization to reduce memory footprint
    def __init__(self, left, right):
        self.left = left
        self.right = right

def create_tree(depth):
    if depth == 0:
        return None
    return Node(create_tree(depth - 1), create_tree(depth - 1))

if __name__ == "__main__":
    depth = 20
    root = create_tree(depth)
    if root:
        print(f"Tree allocated. Depth: {depth}")
