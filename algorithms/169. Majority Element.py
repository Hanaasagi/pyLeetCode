# Given an array of size n, find the majority element. The majority
# element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element
# always exist in the array.


class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num, count = None, 0
        for i in nums:
            if count == 0:
                num, count = i, 1
            elif i == num:
                count += 1
            else:
                count -= 1
        return num
