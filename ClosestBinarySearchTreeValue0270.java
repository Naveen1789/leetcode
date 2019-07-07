/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class ClosestBinarySearchTreeValue0270 {

    private double smallestDiff;
    private int closestVal;


    public void walk(TreeNode r, double t){
        if (r == null){
            return;
        }

        if (Math.abs(r.val - t) <= smallestDiff){
            smallestDiff = Math.abs((double)r.val - t);
            closestVal = r.val;
        }

        walk(r.left, t);
        walk(r.right, t);
    }
    public int closestValue(TreeNode root, double target) {
        smallestDiff = Double.MAX_VALUE;
        closestVal = -1;

        walk(root, target);
        return closestVal;
    }
}
