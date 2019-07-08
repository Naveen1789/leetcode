class MaxStack0716 {

    Stack<Integer> st;
    Stack<Integer> maxStack;

    /** initialize your data structure here. */
    public MaxStack() {
        st = new Stack<Integer>();
        maxStack = new Stack<Integer>();
    }

    public void push(int x) {
        st.push(x);
        if (maxStack.isEmpty() || maxStack.peek() < x){
            maxStack.push(x);
        }
        else {
            maxStack.push(maxStack.peek());
        }
    }

    public int pop() {
        maxStack.pop();
        return st.pop();
    }

    public int top() {
        return st.peek();
    }

    public int peekMax() {
        return maxStack.peek();
    }

    public int popMax() {
        int max = peekMax();
        Stack<Integer> buffer = new Stack<Integer>();
        while (top() != max){
            buffer.push(pop());
        }
        pop();
        while (!buffer.isEmpty()){
            push(buffer.pop());
        }
        return max;
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */
