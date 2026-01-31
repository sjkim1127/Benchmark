
public class Main {
    static class Node {
        Node left, right;
        Node(int depth) {
            if (depth > 0) {
                left = new Node(depth - 1);
                right = new Node(depth - 1);
            }
        }
    }

    public static void main(String[] args) {
        Node root = new Node(20);
        System.out.println("Done");
    }
}
