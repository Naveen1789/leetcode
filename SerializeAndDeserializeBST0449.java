/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class SerializeAndDeserializeBST0449 {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        System.out.println(preOrderTraversal(root));
        return preOrderTraversal(root);
    }

    public String preOrderTraversal(TreeNode node){
        if (node == null) {
            return "";
        }

        String msg = node.val + "";
        if (node.left == null && node.right == null){
            return msg;
        }

        if (node.left == null) {
            msg = msg + "()";
        }
        else {
            msg = msg + "(" + preOrderTraversal(node.left) + ")";
        }

        if (node.right == null){
            return msg;
        }
        else {
            msg = msg + "(" + preOrderTraversal(node.right) + ")";
        }

        return msg;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String s = data;
        if(s == null || s.length() == 0){
            return null;
        }

        Stack<TreeNode> st = new Stack<TreeNode>();

        TreeNode root = null;
        int i = 0;

        int lenOfStr = s.length();
        boolean shouldAssigntoLeft = true;
        while (i < lenOfStr){

            char c = s.charAt(i);
            if (c == '-' || Character.isDigit(c)){
                String num = c + "";
                while (i+1 < lenOfStr && Character.isDigit(s.charAt(i+1))){
                    num = num + s.charAt(i+1);
                    i++;
                }

                TreeNode newNode = new TreeNode(Integer.parseInt(num));
                if(root != null){
                    if(shouldAssigntoLeft && root.left == null){
                        root.left = newNode;
                    }
                    else{
                        root.right = newNode;
                        shouldAssigntoLeft = true;
                    }
                }

                st.push(newNode);
            }
            else if(c == '('){
                root = st.peek();
                if (s.charAt(i+1) == ')'){
                    shouldAssigntoLeft = false;
                    i++;
                }
            }
            else{
                st.pop();
            }
            i++;
        }

        return st.pop();

    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
