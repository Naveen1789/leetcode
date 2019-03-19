"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        if len(root.children) == 0:
            return 1

        curMax = -1

        for child in root.children:
            depth = 1 + self.maxDepth(child)
            if depth > curMax:
                curMax = depth

        return curMax
        
