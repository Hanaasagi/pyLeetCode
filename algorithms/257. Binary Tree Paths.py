# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5

# All root-to-leaf paths are:

# ["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}

    def binaryTreePaths(self, root):
        res = []
        if root is None:
            return res
        stack = [root]
        path_stack = [str(root.val)]

        while len(stack):
            node = stack.pop()
            path = path_stack.pop()
            if node.left is None and node.right is None:
                res.append(path)
                continue
            if node.left is not None:
                stack.append(node.left)
                path_stack.append('{0}->{1}'.format(path, node.left.val))
            if node.right is not None:
                stack.append(node.right)
                path_stack.append('{0}->{1}'.format(path, node.right.val))
        return res
