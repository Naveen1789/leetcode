"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        return self.traverse([root], [])

    def traverse(self, nodesArr, ans):
        if (not nodesArr) or (nodesArr == [None] * len(nodesArr)):
            return ans

        childNodes = []
        levelOrderTraversalArr = []
        for node in nodesArr:
            childNodes = childNodes + node.children
            levelOrderTraversalArr.append(node.val)

        ans.append(levelOrderTraversalArr)
        return self.traverse(childNodes, ans)


        
