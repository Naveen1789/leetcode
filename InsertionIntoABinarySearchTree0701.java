/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class InsertionIntoABinarySearchTree0701 {
    public TreeNode insertIntoBST(TreeNode root, int val) {

        TreeNode curNode = root;
        TreeNode parentOfCurNode = null;

        TreeNode newNode = new TreeNode(val);
        while (curNode != null){
            parentOfCurNode = curNode;
            if (curNode.val < val){
                curNode = curNode.right;
            }
            else{
                curNode = curNode.left;
            }
        }

        if (parentOfCurNode == null){
            return newNode;
        }
        else if(parentOfCurNode.val < val){
            parentOfCurNode.right = newNode;
        }
        else {
            parentOfCurNode.left = newNode;
        }
        return root;
    }
}
