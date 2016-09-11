# Determine whether an integer is a palindrome. Do this without extra space.


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        length = len(s)
        for i in range(length / 2):
            if s[i] != s[length - i - 1]:
                return False
        return True
