class MaximumXOROfTwoNumbersInAnArray0421 {
    int ans = 0;
    public int findMaximumXOR(int[] nums) {
        Node root = new Node();
        for(int num : nums){
            insert(root, num);
        }
        return ans;
    }

    public void insert(Node root, int num){
        int count = 0;
        int curXor = 0;

        Node curNode = root;
        Node nodeWithMaxXor = root;

        // System.out.println("num = " + num);
        // String msg = "";
        while (count < 32){
            count++;
            if(num < 0){
                // System.out.print("1");
                if (curNode.right == null){
                    curNode.right = new Node();
                }
                curNode = curNode.right;

                if (nodeWithMaxXor.left != null){
                    // msg = msg + count + ", ";
                    nodeWithMaxXor = nodeWithMaxXor.left;
                    curXor = curXor + (int)Math.pow(2,(32 - count));
                }
                else{
                    nodeWithMaxXor = nodeWithMaxXor.right;
                }
            }
            else{
                // System.out.print("0");
                if (curNode.left == null){
                    curNode.left = new Node();
                }
                curNode = curNode.left;

                if (nodeWithMaxXor.right != null){
                    // msg = msg + count + ", ";
                    nodeWithMaxXor = nodeWithMaxXor.right;
                    curXor = curXor + (int)Math.pow(2,(32 - count));
                }
                else{
                    nodeWithMaxXor = nodeWithMaxXor.left;
                }
            }
            num = num << 1;
        }

        // System.out.println("\nmsg = " + msg);
        // System.out.println("curXor = " + curXor);
        // System.out.println("***********************");
        if( curXor > ans){
            ans = curXor;
        }
    }
}

class Node {
    Node left;
    Node right;

    Node() {
        this.left = null;
        this.right = null;
    }
}
