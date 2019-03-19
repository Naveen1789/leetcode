# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    

    # def isPalindrome(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     if head == None or head.next == None:
    #         return True
    #
    #     return self.readLinkedList(head) == self.revLinkedList(head)
    #
    # def readLinkedList(self, head):
    #     if head == None:
    #         return ''
    #
    #     return str(head.val) + self.readLinkedList(head.next)
    #
    # def revLinkedList(self, head):
    #     if head == None:
    #         return ''
    #
    #     return self.revLinkedList(head.next) + str(head.val)
