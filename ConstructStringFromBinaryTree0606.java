/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class ConstructStringFromBinaryTree0606 {
    public String tree2str(TreeNode t) {
        return preOrderTraversal(t);
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
}
