# Given a linked list, remove the nth node from the end of list and return
# its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes
# 1->2->3->5.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr1 = head
        ptr2 = head
        for _ in range(0, n):
            ptr2 = ptr2.next
        # remove head node
        if ptr2 is None:
            return head.next
        while ptr2.next is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = ptr1.next.next
        return head
