# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# For example:
# Given the below binary tree and sum = 22,

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1

# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        from __builtin__ import sum as _sum
        if root is None:
            return False
        stack = [root]
        path_stack = [(root.val,)]

        while len(stack):
            node = stack.pop()
            path_sum = _sum(path_stack.pop())
            if node.left is None and node.right is None and path_sum == sum:
                return True
            if node.left is not None:
                stack.append(node.left)
                path_stack.append((path_sum, node.left.val))
            if node.right is not None:
                stack.append(node.right)
                path_stack.append((path_sum, node.right.val))
        return False
