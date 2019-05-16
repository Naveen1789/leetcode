# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        return self.arePresentAndAreCousins([root], x, y)

    def arePresentAndAreCousins(self, listOfNodes, x, y):
        if len(listOfNodes) == 0:
            return False
        numberOfNodes = len(listOfNodes)
        i = 0
        index1 = -1
        index2 = -1
        while i < numberOfNodes:
            if (listOfNodes[i] != None) and (listOfNodes[i].val == x or listOfNodes[i].val == y):
                if index1 == -1:
                    index1 = i
                else:
                    index2 = i
            i = i+1

        if index1 == -1 and index2 == -1:
            childNodes = []
            for node in listOfNodes:
                if node != None:
                    childNodes.append(node.left)
                    childNodes.append(node.right)
            return self.arePresentAndAreCousins(childNodes, x, y)

        elif index1 == -1 or index2 == -1:
            return False

        else:
            if abs(index1 - index2) == 1:
                if index1 < index2:
                    if index1 % 2 == 0:
                        return False
                else:
                    if index2 % 2 == 0:
                        return False
            return True
