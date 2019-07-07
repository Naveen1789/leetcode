/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class SubTreeOfAnotherTree0572 {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        return inOrderTraversal(s).contains(inOrderTraversal(t));
    }

    public String inOrderTraversal(TreeNode n) {
        if (n == null){
            return "*";
        }
        if (n.left == null && n.right == null)
        {
            return "(" + n.val + ")";
        }
        return inOrderTraversal(n.left) + n.val + inOrderTraversal(n.right);
    }
}
