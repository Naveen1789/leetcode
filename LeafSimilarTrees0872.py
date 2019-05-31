# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leafNodesForRoot1 = []
        leafNodesForRoot2 = []

        self.getLeafNodesInOrder(root1, leafNodesForRoot1)
        self.getLeafNodesInOrder(root2, leafNodesForRoot2)

        return leafNodesForRoot1 == leafNodesForRoot2

    def getLeafNodesInOrder(self, root, ans):
        if root == None:
            return
        if root.left == None and root.right == None:
            ans.append(root.val)
        self.getLeafNodesInOrder(root.left, ans)
        self.getLeafNodesInOrder(root.right, ans)
