/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class ConstructBinaryTreeFromPreorderAndInorderTraversal0105 {

    int preOrderIndex = 0;
    int[] preorder;
    int[] inorder;
    HashMap<Integer, Integer> indexMap = new HashMap<Integer, Integer>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;

        for (int i = 0; i < inorder.length; i++){
            indexMap.put(inorder[i], i);
        }
        return helper (0, inorder.length-1);

    }

    public TreeNode helper(int left, int right){
        if (left > right) {
            return null;
        }

        int rootVal = preorder[preOrderIndex];
        TreeNode root = new TreeNode(rootVal);

        preOrderIndex++;
        root.left = helper(left, indexMap.get(rootVal) - 1);
        root.right = helper(indexMap.get(rootVal) + 1, right);

        return root;
    }
}
