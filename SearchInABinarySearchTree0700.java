/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class SearchInABinarySearchTree0700 {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null || root.val == val){
            return root;
        }

        if(val > root.val){
            return searchBST(root.right, val);
        }
        else{
            return searchBST(root.left, val);
        }
    }
}
