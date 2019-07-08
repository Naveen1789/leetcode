class LRUCache0146 {   
    class DoublyLinkedListNode{
        int key;
        int val;
        DoublyLinkedListNode prev;
        DoublyLinkedListNode next;
    }

    public void addNode(DoublyLinkedListNode newNode){
        newNode.prev = head;
        newNode.next = head.next;

        head.next.prev = newNode;
        head.next = newNode;
    }

    public void removeNode(DoublyLinkedListNode node){
        DoublyLinkedListNode prevNode = node.prev;
        DoublyLinkedListNode nextNode = node.next;

        node.prev.next = nextNode;
        node.next.prev = prevNode;
    }

    public void moveToHead(DoublyLinkedListNode node) {
        removeNode(node);
        addNode(node);
    }

    public DoublyLinkedListNode popTail(){
        DoublyLinkedListNode lastNode = tail.prev;
        removeNode(lastNode);
        return lastNode;
    }

    HashMap<Integer, DoublyLinkedListNode> cache = new HashMap<Integer, DoublyLinkedListNode>();

    int size;
    int capacity;

    DoublyLinkedListNode head;
    DoublyLinkedListNode tail;

    public LRUCache(int capacity) {
        this.size = 0;
        this.capacity = capacity;
        this.head = new DoublyLinkedListNode();
        this.tail = new DoublyLinkedListNode();
        this.head.next = tail;
        this.tail.prev = head;
    }

    public int get(int key) {
        DoublyLinkedListNode node = cache.get(key);

        if (node == null){
            return -1;
        }
        else {
            moveToHead(node);
            return node.val;
        }

    }

    public void put(int key, int value) {
        DoublyLinkedListNode node = cache.get(key);
        if (node == null){
            DoublyLinkedListNode nodeToBeAdded = new DoublyLinkedListNode();
            nodeToBeAdded.key = key;
            nodeToBeAdded.val = value;

            cache.put(key, nodeToBeAdded);
            addNode(nodeToBeAdded);
            size++;

            if(size > capacity){
                DoublyLinkedListNode prevTail = popTail();
                cache.remove(prevTail.key);

                size--;
            }
        }
        else {
            node.val = value;
            moveToHead(node);
        }

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
