# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        return self.computeLevelOrderTraversal([root], [])

    def computeLevelOrderTraversal(self, listOfNodesAtThisLevel, ans):
        if listOfNodesAtThisLevel == None or len(listOfNodesAtThisLevel) == 0:
            return ans
        childNodes = []
        traversedNodes = []
        for node in listOfNodesAtThisLevel:
            if node == None:
                continue
            traversedNodes.append(node.val)
            if node.left != None:
                childNodes.append(node.left)
            if node.right != None:
                childNodes.append(node.right)

        ans.append(traversedNodes)
        return self.computeLevelOrderTraversal(childNodes, ans)
        
