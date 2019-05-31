# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.findIfBalanced(root)


    def findIfBalanced(self, node):
        if node == None or (node.left == None and node.right == None):
            return True

        depthOfLeftSubTree = self.findHeightOfNode(node.left)
        depthOfRightSubTree = self.findHeightOfNode(node.right)

        return (abs(depthOfLeftSubTree - depthOfRightSubTree) < 2) and self.findIfBalanced(node.left) and self.findIfBalanced(node.right)


    def findHeightOfNode(self, node):
        if node == None:
            return 0
        else:
            return max(self.findHeightOfNode(node.left), self.findHeightOfNode(node.right)) + 1



        
