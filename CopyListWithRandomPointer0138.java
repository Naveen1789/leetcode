/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;
    public Node random;

    public Node() {}

    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }

        if (head.next == null) {
            Node headOfCopy = new Node(head.val, null, null);
            if (head.random != null) {
                headOfCopy.random = headOfCopy;
            }
            return headOfCopy;
        }

        Node headOfOriginal = head;
        while (headOfOriginal != null) {
            Node newNodeInCopy = new Node(headOfOriginal.val, headOfOriginal.next, null);
            headOfOriginal.next = newNodeInCopy;
            headOfOriginal = newNodeInCopy.next;
        }

        headOfOriginal = head;
        while (headOfOriginal != null) {
            headOfOriginal.next.random = (headOfOriginal.random == null) ? null : headOfOriginal.random.next;
            headOfOriginal = headOfOriginal.next.next;
        }

        Node copy = head.next;
        Node curNode = head;
        while (curNode.next != null){
            Node nodeToBeSkipped = curNode.next;
            curNode.next = curNode.next.next;
            curNode = nodeToBeSkipped;
        }

        return copy;
    }
}
