# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if fast == None or fast.next == None:
            return None

        newPtr = head
        while newPtr != slow:
            newPtr = newPtr.next
            slow = slow.next

        return slow
        
    # def detectCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     visited = []
    #     slow = head
    #     fast = head
    #
    #     while True:
    #         if fast == None or fast.next == None:
    #             return None
    #         if slow in visited:
    #             return slow
    #
    #         visited.append(slow)
    #         slow = slow.next
    #         fast = fast.next.next

    # def detectCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     visited = []
    #     slow = head
    #
    #     while True:
    #         if slow == None:
    #             return None
    #         if slow in visited:
    #             return slow
    #
    #         visited.append(slow)
    #         slow = slow.next
