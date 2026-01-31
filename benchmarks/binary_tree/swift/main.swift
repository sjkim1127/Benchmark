
class Node {
    var left: Node?
    var right: Node?
    init(_ depth: Int) {
        if depth > 0 {
            left = Node(depth - 1)
            right = Node(depth - 1)
        }
    }
}

let root = Node(20)
print("Done")
