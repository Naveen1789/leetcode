# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q == None):
            return True
        if (p == None or q == None) or (p.val != q.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # altrnate solution
        # return (self.inOrder(p) == self.inOrder(q)) and (self.preOrder(p) == self.preOrder(q))


    def inOrder(self, root):
        if root == None:
            return '*'
        return self.inOrder(root.left) + str(root.val) + self.inOrder(root.right)

    def preOrder(self, root):
        if root == None:
            return '*'
        return str(root.val) + self.preOrder(root.left) + self.preOrder(root.right)
