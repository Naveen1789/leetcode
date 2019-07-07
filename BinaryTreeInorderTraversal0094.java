/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BinaryTreeInorderTraversal0094 {
  // Morris traversal - from Solution
  public List < Integer > inorderTraversal(TreeNode root) {
      List < Integer > res = new ArrayList < > ();
      TreeNode curr = root;
      TreeNode pre;
      while (curr != null) {
          if (curr.left == null) {
              res.add(curr.val);
              curr = curr.right; // move to next right node
          } else { // has a left subtree
              pre = curr.left;
              while (pre.right != null) { // find rightmost
                  pre = pre.right;
              }
              pre.right = curr; // put cur after the pre node
              TreeNode temp = curr; // store cur node
              curr = curr.left; // move cur to the top of the new tree
              temp.left = null; // original cur left be null, avoid infinite loops
          }
      }
      return res;
  }

// Using recursion -
    //     public List<Integer> inorderTraversal(TreeNode root) {
    //         List<Integer> inOrder = new ArrayList<Integer>();

    //         return inOrderTraversal(root, inOrder);
    //     }

    //     public List<Integer> inOrderTraversal(TreeNode node, List<Integer> pathSoFar) {
    //         if (node != null){
    //             inOrderTraversal(node.left, pathSoFar);
    //             pathSoFar.add(node.val);
    //             inOrderTraversal(node.right, pathSoFar);
    //         }
    //         return pathSoFar;
    //     }


// Using stacks -

    // public List<Integer> inorderTraversal(TreeNode root) {
    //     List<Integer> inOrder = new ArrayList<Integer>();
    //     return inOrderTraversalUsingStack(root, inOrder);
    // }
    //
    // public List<Integer> inOrderTraversalUsingStack(TreeNode root, List<Integer> pathSoFar){
    //     Stack<TreeNode> st = new Stack<TreeNode> ();
    //
    //     while (root != null || !st.isEmpty()){
    //         while (root != null){
    //             st.push(root);
    //             root = root.left;
    //         }
    //
    //         root = st.pop();
    //         pathSoFar.add(root.val);
    //         root = root.right;
    //     }
    //
    //     return pathSoFar;
    // }
}
