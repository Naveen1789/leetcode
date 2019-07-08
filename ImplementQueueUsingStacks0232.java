class ImplementQueueUsingStacks0232 {

    int front;
    Stack<Integer> s1;
    Stack<Integer> s2;

    /** Initialize your data structure here. */
    public MyQueue() {
        s1 = new Stack<Integer>();
        s2 = new Stack<Integer>();
    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        if (s1.empty()){
            front = x;
        }
        while (!s1.empty()){
            s2.push(s1.pop());
        }

        s2.push(x);

        while (!s2.empty()){
            s1.push(s2.pop());
        }


    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        int poppedElem = s1.pop();
        if (!s1.empty()){
            front = s1.peek();
        }
        return poppedElem;
    }

    /** Get the front element. */
    public int peek() {
        return front;
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return s1.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
