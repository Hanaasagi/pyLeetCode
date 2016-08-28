# Given a linked list, return the node where the cycle begins. If there is
# no cycle, return null.

# Note: Do not modify the linked list.

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
        if head is None:
            return None
        slow = fast = head
        hasCycle = False
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                hasCycle = True
                slow = head
                break
        if not hasCycle:
            return None
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
