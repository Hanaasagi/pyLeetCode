# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a
# single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

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
        node = ListNode(None)
        head = node
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            node.next = ListNode(s % 10)
            carry = s / 10
            l1 = l1.next
            l2 = l2.next
            node = node.next

        while l1:
            s = l1.val + carry
            node.next = ListNode(s % 10)
            carry = s / 10
            l1 = l1.next
            node = node.next
        while l2:
            s = l2.val + carry
            node.next = ListNode(s % 10)
            carry = s / 10
            l2 = l2.next
            node = node.next
        node.next = ListNode(carry) if carry else None
        return head.next
