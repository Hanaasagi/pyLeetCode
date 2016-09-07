# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1
# as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or
# equal to m + n) to hold additional elements from nums2. The number of
# elements initialized in nums1 and nums2 are m and n respectively.

# Subscribe to see which companies asked this question


class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m - 1
        ptr2 = n - 1
        ptr = m + n - 1
        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            ptr -= 1
        while ptr2 >= 0:
            nums1[ptr] = nums2[ptr2]
            ptr -= 1
            ptr2 -= 1
