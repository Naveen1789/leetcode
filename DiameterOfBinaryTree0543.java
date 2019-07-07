/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class DiameterOfBinaryTree0543 {
  private int diameter = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        lengthOfLongestPath(root);
        return diameter;
    }

    public int lengthOfLongestPath (TreeNode node){
        if (node == null || (node.left == null && node.right == null)) {
            return 0;
        }
        else{
            int longestPathThroughThisNode = 0;
            int longestPathStartingFromLeftChild = lengthOfLongestPath(node.left);
            int longestPathStartingFromRightChild = lengthOfLongestPath(node.right);

            if (node.left == null){
                longestPathThroughThisNode = 1 + longestPathStartingFromRightChild;
            }
            else if (node.right == null){
                longestPathThroughThisNode = 1 + longestPathStartingFromLeftChild;
            }
            else {
                longestPathThroughThisNode = 2 + longestPathStartingFromRightChild + longestPathStartingFromLeftChild;
            }

            diameter = Math.max(longestPathThroughThisNode, diameter);
            return 1 + Math.max(longestPathStartingFromLeftChild, longestPathStartingFromRightChild);
        }
    }
    
    // private int diameter = 0;
    // public int diameterOfBinaryTree(TreeNode root) {
    //     inOrderTraversal(root);
    //     return diameter;
    // }
    //
    // public void inOrderTraversal(TreeNode node){
    //     if (node == null){
    //         return;
    //     }
    //
    //     inOrderTraversal(node.left);
    //
    //     int longestPathThroughThisNode = 0;
    //     if (node.left == null && node.right == null){
    //         longestPathThroughThisNode = 0;
    //     }
    //     else if (node.left == null) {
    //         longestPathThroughThisNode = 1 + lengthOfLongestPath(node.right);
    //     }
    //     else if (node.right == null) {
    //         longestPathThroughThisNode = 1 + lengthOfLongestPath(node.left);
    //     }
    //     else {
    //         longestPathThroughThisNode = 2 + lengthOfLongestPath(node.left) + lengthOfLongestPath(node.right);
    //     }
    //
    //     if (longestPathThroughThisNode > diameter) {
    //         diameter = longestPathThroughThisNode;
    //     }
    //     inOrderTraversal(node.right);
    // }
    //
    // public int lengthOfLongestPath (TreeNode node){
    //     if (node == null || (node.left == null && node.right == null)) {
    //         return 0;
    //     }
    //     else{
    //         return 1 + Math.max(lengthOfLongestPath(node.left), lengthOfLongestPath(node.right));
    //     }
    // }
}
