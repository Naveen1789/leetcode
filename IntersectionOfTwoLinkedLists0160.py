# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lengthOfA = self.findLengthOfLinkedList(headA)
        lengthOfB = self.findLengthOfLinkedList(headB)

        while lengthOfA > lengthOfB:
            headA = headA.next
            lengthOfA = lengthOfA - 1

        while lengthOfB > lengthOfA:
            headB = headB.next
            lengthOfB = lengthOfB - 1

        while headA != None and headB != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def findLengthOfLinkedList(self, head):
        length = 0
        while head != None:
            length = length + 1
            head = head.next
        return length
