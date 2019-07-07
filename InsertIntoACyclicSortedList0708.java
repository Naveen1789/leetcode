/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val,Node _next) {
        val = _val;
        next = _next;
    }
};
*/
class InsertIntoACyclicSortedList0708 {
    public Node insert(Node head, int insertVal) {
        Node curNode = head;
        Node largestNode = head;
        Node newNode = new Node(insertVal);

        if (head == null){
            newNode.next = newNode;
            return newNode;
        }

        do {
            if (insertVal >= curNode.val && curNode.next.val >= insertVal){
                newNode.next = curNode.next;
                curNode.next = newNode;
                return head;
            }
            if (curNode.val >= largestNode.val){
                largestNode = curNode;
            }
            curNode = curNode.next;
        } while (curNode != head);

        newNode.next = largestNode.next;
        largestNode.next = newNode;
        return head;
    }
}
