# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length. 


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        length = len(nums)
        i = 1
        while i < length:
            if nums[i] == nums[i - 1]:
                flag += 1
                if flag > 1:
                    del nums[i]
                    i -= 1
                    length -= 1
            else:
                flag = 0
            i += 1
        return length
