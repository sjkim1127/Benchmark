enum Node {
    Leaf,
    Branch(Box<Node>, Box<Node>),
}

fn create_tree(depth: i32) -> Node {
    if depth == 0 {
        return Node::Leaf;
    }
    Node::Branch(
        Box::new(create_tree(depth - 1)),
        Box::new(create_tree(depth - 1)),
    )
}

fn main() {
    let depth = 20;
    let root = create_tree(depth);
    if let Node::Branch(_, _) = root {
        println!("Tree allocated. Depth: {}", depth);
    }
    // Drop happens automatically here
}
