# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        negative = False
        if x < 0:
            negative = True
            x = -x
        while x:
            rev = rev * 10 + x % 10
            x = x / 10
        if rev > (2**31) - 1:
            return 0
        return -rev if negative else rev
