/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class SumOfRootToLeafBinaryNumbers1022 {
    int ans = 0;
    public int sumRootToLeaf(TreeNode root) {
        ArrayList<Integer> nodeVals = new ArrayList<Integer>();
        traverseNodeToLeaf(root, nodeVals);

        return ans;

    }

    public void traverseNodeToLeaf(TreeNode node, ArrayList<Integer> nodeVals){
        // System.out.println("powOfTwo->" + powOfTwo);
        if (node == null){
            return;
        }

        if (node.left == null && node.right == null){
            int i = nodeVals.size() - 1;
            int powOfTwo = 1;
            int sum = node.val;
            while (i >= 0){
                sum = sum + ((int)Math.pow(2, powOfTwo) * nodeVals.get(i));
                powOfTwo++;
                i--;
            }
            ans = ans + sum;
        }
        else{
            nodeVals.add(node.val);
            traverseNodeToLeaf(node.left, nodeVals);
            traverseNodeToLeaf(node.right, nodeVals);
            nodeVals.remove(nodeVals.size() - 1);
        }
    }
}


// class SumOfRootToLeafBinaryNumbers1022 {
//     int ans = 0;
//     public int sumRootToLeaf(TreeNode root) {
//         traverseNodeToLeaf(root, 0);
//         return ans;
//     }
//
//     public void traverseNodeToLeaf(TreeNode node, int sum){
//         if (node == null){
//             return;
//         }
//
//         if (node.left == null && node.right == null){
//             sum = (sum * 2) + node.val;
//             ans = ans + sum;
//             return;
//         }
//
//         traverseNodeToLeaf(node.left, (sum * 2) + node.val);
//         traverseNodeToLeaf(node.right, (sum * 2) + node.val);
//     }
// }
