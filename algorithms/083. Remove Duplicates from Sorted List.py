# Given a sorted linked list, delete all duplicates such that each element
# appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

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
        if head is None:
            return head
        node = head
        preNode = node
        while node.next is not None:
            node = node.next
            if node.val == preNode.val:
                preNode.next = node.next
            else:
                preNode = preNode.next
        return head
