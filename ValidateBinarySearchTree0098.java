/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class ValidateBinarySearchTree0098 {
    private TreeNode prevLeftNode;
    private boolean isValidBst = true;

    public boolean isValidBST(TreeNode root) {
        inorderWalk(root);

        return isValidBst;
    }

    public void inorderWalk(TreeNode root) {

        if(root == null){
            return;
        }

        inorderWalk(root.left);

        if (prevLeftNode != null && prevLeftNode.val >= root.val){
            isValidBst = false;
        }
        prevLeftNode = root;

        inorderWalk(root.right);
    }
}
