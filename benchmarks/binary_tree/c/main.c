#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    struct Node *left;
    struct Node *right;
} Node;

Node* create_tree(int depth) {
    if (depth == 0) return NULL;
    Node* node = (Node*)malloc(sizeof(Node));
    node->left = create_tree(depth - 1);
    node->right = create_tree(depth - 1);
    return node;
}

void free_tree(Node* node) {
    if (node == NULL) return;
    free_tree(node->left);
    free_tree(node->right);
    free(node);
}

int main() {
    int depth = 20;
    Node* root = create_tree(depth);
    // verification (trivial)
    if (root) printf("Tree allocated. Depth: %d\n", depth);
    free_tree(root);
    return 0;
}
