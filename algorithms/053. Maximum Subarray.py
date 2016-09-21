# Find the contiguous subarray within an array (containing at least one
# number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempSum = 0
        maxSum = nums[0]
        for num in nums:
            tempSum += num
            if tempSum > maxSum:
                maxSum = tempSum
            if tempSum < 0:
                tempSum = 0
        return maxSum
