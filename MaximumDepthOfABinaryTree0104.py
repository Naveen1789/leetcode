# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        if (leftMax > rightMax):
            return 1 + leftMax
        else:
            return 1 + rightMax
