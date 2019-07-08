/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class ConstructBinaryTreeFromPreorderAndPostorderTraversal0889 {
    int[] pre;
    int[] post;
    public TreeNode constructFromPrePost(int[] pre, int[] post) {

        if (pre == null || pre.length == 0){
            return null;
        }

        TreeNode root = new TreeNode(pre[0]);
        if (pre.length == 1){
            return root;
        }

        int L = 0;

        for (int i = 0; i < post.length; i++){
            if (pre[1] == post[i]){
                L = i+1;
                break;
            }
        }


        root.left = constructFromPrePost(Arrays.copyOfRange(pre, 1, L+1), Arrays.copyOfRange(post, 0,L));
        root.right = constructFromPrePost(Arrays.copyOfRange(pre, L+1, pre.length), Arrays.copyOfRange(post, L,post.length-1));


        return root;
    }

}
