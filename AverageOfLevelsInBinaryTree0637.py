# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        return self.getAverageAtEachLevel([root], [])

    def getAverageAtEachLevel(self, listOfNodesAtThisLevel, ans):
        if listOfNodesAtThisLevel == None or len(listOfNodesAtThisLevel) == 0:
            return ans
        sum = 0
        childNodes = []
        for node in listOfNodesAtThisLevel:
            sum = sum + node.val
            if node.left != None:
                childNodes.append(node.left)
            if node.right != None:
                childNodes.append(node.right)

        ans.append(float(sum) / len(listOfNodesAtThisLevel))
        return self.getAverageAtEachLevel(childNodes, ans)
        
