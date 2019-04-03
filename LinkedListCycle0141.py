# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False

        slow = head
        fast = head

        while True:
            slow = slow.next
            fast = fast.next
            if fast == None:
                return False
            fast = fast.next

            if slow == fast or fast == None:
                return fast != None

        
