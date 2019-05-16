# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curNode = head
        while curNode != None and curNode.next != None:
            if curNode.val == curNode.next.val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next

        return head
        
