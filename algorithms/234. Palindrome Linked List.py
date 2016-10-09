# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        rhead = self.reverseList(slow.next)
        while rhead is not None:
            if head.val != rhead.val:
                return False
            head = head.next
            rhead = rhead.next
        return True

    def reverseList(self, node):
        next = None
        while node is not None:
            temp = node.next
            node.next = next
            next = node
            node = temp
        return next
