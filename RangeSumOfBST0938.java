/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class RangeSumOfBST0938 {
    int sum = 0;
    public int rangeSumBST(TreeNode root, int L, int R) {
        inOrderTraversal(root, L, R);
        return sum;
    }

    public void inOrderTraversal(TreeNode node, int L, int R) {
        if (node == null){
            return;
        }

        if (node.val < L){
            inOrderTraversal(node.right, L, R);
        }

        else if (node.val > R){
            inOrderTraversal(node.left, L, R);
        }

        else{
            sum = sum + node.val;
            inOrderTraversal(node.left, L, R);
            inOrderTraversal(node.right, L, R);
        }


    }
}
