# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True

        # get count
        numOfNodes = self.getLinkedListLength(head)
        mid = numOfNodes / 2

        # read first half from left to right
        firstPart = self.readLinkedListFromLeftToRight(head, mid)

        # pass thorugh first part
        node = head
        iter = 0
        if numOfNodes % 2 == 0:
            count = mid
        else:
            count = mid + 1

        while iter < count:
            node = node.next
            iter = iter + 1

        # read second part from right to left
        secondPart = self.readLinkedListFromRightToLeft(node)
        # print firstPart
        # print secondPart
        return firstPart == secondPart

    def getLinkedListLength(self, node):
        count = 0
        while node != None:
            count = count + 1
            node = node.next
        return count


    def readLinkedListFromLeftToRight(self, node, k):
        ans = ""
        iter = 0
        while iter < k:
            ans = ans + '*' + str(node.val)
            node = node.next
            iter = iter + 1

        ans = ans + '*'
        return ans

    def readLinkedListFromRightToLeft(self, node):
        ans = ""
        while node != None:
            ans = str(node.val) + "*" + ans
            node = node.next
        ans = '*' + ans
        return ans


# Alternate solution
# Read number of nodes
# Go to the mid-point
# Reverse the second half of linked list
# Now compare the first half and second half
