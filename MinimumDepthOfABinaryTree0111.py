# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        if root.left == None:
            return 1 + self.minDepth(root.right)

        if root.right == None:
            return 1 + self.minDepth(root.left)

        leftMin = self.minDepth(root.left)
        rightMin = self.minDepth(root.right)
        if (leftMin < rightMin):
            return 1 + leftMin
        else:
            return 1 + rightMin
