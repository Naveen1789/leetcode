# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumOfLeftLeafNodes(root, False, 0)


    def sumOfLeftLeafNodes(self, node, isLeft, sumSoFar):
        if node == None:
            return sumSoFar
        if node.left == None and node.right == None and isLeft:
            sumSoFar = sumSoFar + node.val
            return sumSoFar

        return self.sumOfLeftLeafNodes(node.left, True, sumSoFar) + self.sumOfLeftLeafNodes(node.right, False, sumSoFar)
