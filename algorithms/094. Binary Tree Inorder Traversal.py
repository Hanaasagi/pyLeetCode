# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],

#    1
#     \
#      2
#     /
#    3

# return [1,3,2].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def traversal(root):
            if root is None:
                return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        traversal(root)
        return res
