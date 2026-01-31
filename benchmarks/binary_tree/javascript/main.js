class Node {
    constructor(left, right) {
        this.left = left;
        this.right = right;
    }
}

function createTree(depth) {
    if (depth === 0) return null;
    return new Node(createTree(depth - 1), createTree(depth - 1));
}

const depth = 20;
const root = createTree(depth);
if (root) {
    console.log(`Tree allocated. Depth: ${depth}`);
}
