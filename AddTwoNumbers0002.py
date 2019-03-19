# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return l1
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        carry = 0
        head = None
        curHead = None

        while (l1 != None or l2 != None):
            temp = carry
            if l1 != None:
                temp = temp + l1.val
                l1 = l1.next
            if l2 != None:
                temp = temp + l2.val
                l2 = l2.next
            newNode = ListNode(temp % 10)
            if head != None:
                curHead.next = newNode
                curHead = newNode
            else:
                head = newNode
                curHead = newNode

            carry = temp / 10

        if carry == 1:
            newNode = ListNode(1)
            curHead.next = newNode

        return head
