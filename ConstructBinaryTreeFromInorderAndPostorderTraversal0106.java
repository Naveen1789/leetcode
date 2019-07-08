/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class ConstructBinaryTreeFromInorderAndPostorderTraversal0106 {
    int postOrderIndex = 0;
    int[] postorder;
    int[] inorder;
    HashMap<Integer, Integer> indexMap = new HashMap<Integer, Integer>();

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        this.postorder = postorder;
        this.inorder = inorder;

        this.postOrderIndex = postorder.length - 1;

        for (int i = 0; i < inorder.length; i++){
            indexMap.put(inorder[i], i);
        }
        return helper (0, inorder.length-1);
    }

    public TreeNode helper(int left, int right){
        if (left > right) {
            return null;
        }

        int rootVal = postorder[postOrderIndex];
        TreeNode root = new TreeNode(rootVal);

        postOrderIndex--;
        root.right = helper(indexMap.get(rootVal) + 1, right);
        root.left = helper(left, indexMap.get(rootVal) - 1);

        return root;
    }
}
