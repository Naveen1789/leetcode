# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        first = l1
        second = l2
        if first.val < second.val:
            ans = first
            first = first.next
        else:
            ans = second
            second = second.next

        curNode = ans
        while first != None and second != None:
            if first.val < second.val:
                curNode.next = first
                curNode = first
                first = first.next
            else:
                curNode.next = second
                curNode = second
                second = second.next

        if first != None:
            curNode.next = first

        if second != None:
            curNode.next = second

        return ans
