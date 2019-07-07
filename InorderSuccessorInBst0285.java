/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

 /**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class InorderSuccessorInBst0285 {
    private TreeNode prevLeftNode;

    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {

        if(root == null){
            return null;
        }

        TreeNode left = inorderSuccessor(root.left, p);
        if (left != null){
            return left;
        }

        if (prevLeftNode == p){
            return root;
        }
        prevLeftNode = root;

        TreeNode right = inorderSuccessor(root.right, p);
        if (right != null){
            return right;
        }

        return null;
    }
}

// class InorderSuccessorInBst0285 {
//     private int smallestDiff;
//     private TreeNode successor;
//
//     public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
//         smallestDiff = Integer.MAX_VALUE;
//         successor = null;
//
//         walk(root, p);
//
//         return successor;
//     }
//
//     public void walk(TreeNode r, TreeNode p){
//         if (r == null){
//             return;
//         }
//
//         if (r.val > p.val){
//             if ((r.val - p.val) < smallestDiff){
//                 smallestDiff = (r.val - p.val);
//                 successor = r;
//             }
//             walk(r.left, p);
//         }
//         else{
//             walk(r.right, p);
//         }
//     }
// }
