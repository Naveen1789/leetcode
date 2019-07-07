/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class MostFrequentSubTreeSum0508 {
    HashMap<Integer, Integer> hMap = new HashMap<Integer, Integer>();
    int freqOfMostFrequentSum = 0;
    public int[] findFrequentTreeSum(TreeNode root) {
        findSumOfTree(root);

        int count = 0;
        for (Map.Entry<Integer,Integer> entry : hMap.entrySet()) {
            if (entry.getValue() == freqOfMostFrequentSum){
                count++;
            }
        }
        int[] ans = new int[count];

        int i = 0;
        for (Map.Entry<Integer,Integer> entry : hMap.entrySet()) {
            if (entry.getValue() == freqOfMostFrequentSum){
                ans[i] = entry.getKey();
                i = i+1;
            }
        }

        return ans;

    }

    public int findSumOfTree(TreeNode n) {
        int sum = 0;

        if (n == null){
            return 0;
        }

        else if (n.left == null && n.right == null){
            sum = n.val;
        }

        else {
            if (n.left != null){
                sum = sum + findSumOfTree(n.left);
            }

            if (n.right != null){
                sum = sum + findSumOfTree(n.right);
            }

            sum = sum + n.val;
        }

        if (hMap.containsKey(sum)){
            hMap.put(sum, hMap.get(sum) + 1);
        }
        else{
            hMap.put(sum, 1);
        }
        if (hMap.get(sum) > freqOfMostFrequentSum) {
            freqOfMostFrequentSum = hMap.get(sum);
        }

        return sum;
    }
}
