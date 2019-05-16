# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head != None and head.val == val:
            head = head.next

        curNode = head
        while curNode != None:
            if curNode.next != None and curNode.next.val == val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next

        return head
