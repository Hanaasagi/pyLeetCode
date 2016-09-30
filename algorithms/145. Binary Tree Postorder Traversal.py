# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},

#    1
#     \
#      2
#     /
#    3

# return [3,2,1].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def traversal(node):
            if node is None:
                return
            traversal(node.left)
            traversal(node.right)
            res.append(node.val)
        traversal(root)
        return res
