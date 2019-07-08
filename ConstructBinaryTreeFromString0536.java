/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class ConstructBinaryTreeFromString0536 {
    public TreeNode str2tree(String s) {

        if(s == null || s.length() == 0){
            return null;
        }

        Stack<TreeNode> st = new Stack<TreeNode>();

        TreeNode root = null;
        int i = 0;

        int lenOfStr = s.length();
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
                    if(root.left == null){
                        root.left = newNode;
                    }
                    else{
                        root.right = newNode;
                    }
                }

                st.push(newNode);
            }
            else if(c == '('){
                root = st.peek();
            }
            else{
                st.pop();
            }
            i++;
        }

        return st.pop();

    }
}
