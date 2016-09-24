# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:

# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # list is unhashable in python 2
        # history = set()
        history = []
        res = []

        for i, n in enumerate(nums):
            if n not in history:
                history.append(n)
                res += [[n] + p for p in self.permuteUnique(nums[:i] + nums[i+1:]) or [[]]]
        return res
