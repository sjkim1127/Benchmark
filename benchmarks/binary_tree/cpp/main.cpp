#include <iostream>

struct Node {
    Node *left;
    Node *right;
    
    Node(Node* l, Node* r) : left(l), right(r) {}
    ~Node() {
        delete left;
        delete right;
    }
};

Node* create_tree(int depth) {
    if (depth == 0) return nullptr;
    return new Node(create_tree(depth - 1), create_tree(depth - 1));
}

int main() {
    int depth = 20;
    Node* root = create_tree(depth);
    if (root) std::cout << "Tree allocated. Depth: " << depth << std::endl;
    delete root; // Recursive delete via destructor
    return 0;
}
