import java.util.LinkedList;

class ImplementStackUsingQueues0225 {
    LinkedList<Integer> q1;
    LinkedList<Integer> q2;
    int top;
    /** Initialize your data structure here. */
    public MyStack() {
        q1 = new LinkedList<Integer>();
        q2 = new LinkedList<Integer>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        q2.add(x);
        top = x;

        while(!q1.isEmpty()){
            q2.add(q1.remove());
        }
        while(!q2.isEmpty()){
            q1.add(q2.remove());
        }
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int poppedElem = q1.remove();
        if (!q1.isEmpty()){
            top = q1.peek();
        }
        return poppedElem;
    }

    /** Get the top element. */
    public int top() {
        return top;
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return q1.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
