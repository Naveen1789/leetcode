# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        self.findAllPaths(root, "", ans)
        return ans

    def findAllPaths(self, node, currentPath, ans):
        if node == None:
            return ans
        elif node.left == None and node.right == None:
            if currentPath == "" or currentPath == None:
                currentPath = str(node.val)
            else:
                currentPath = currentPath + "->" + str(node.val)
            ans.append(currentPath)

        else:
            if currentPath == "" or currentPath == None:
                currentPath = str(node.val)
            else:
                currentPath = currentPath + "->" + str(node.val)
            self.findAllPaths(node.left, currentPath, ans)
            self.findAllPaths(node.right, currentPath, ans)
