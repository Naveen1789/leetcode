/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class CountUnivalueSubTrees0250 {
    int numberOfUniValSubtrees = 0;
    public int countUnivalSubtrees(TreeNode root) {
       isUnivalSubTree(root);
        return numberOfUniValSubtrees;
    }

    public boolean isUnivalSubTree(TreeNode n){
        if (n == null){
            return false;
        }

        if (n.left == null && n.right == null){
            numberOfUniValSubtrees = numberOfUniValSubtrees + 1;
            return true;
        }

        boolean isUnival = true;
        if (n.left != null){
            if (! (isUnivalSubTree(n.left) && n.val == n.left.val)) {
                isUnival = false;
            }
        }

        if (n.right != null){
            if (! (isUnivalSubTree(n.right) && n.val == n.right.val)) {
                isUnival = false;
            }
        }

        if (isUnival){
            numberOfUniValSubtrees = numberOfUniValSubtrees + 1;
            return true;
        }
        else {
            return false;
        }
    }
}
