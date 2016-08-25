# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res, p = 0, 'I'
        for i in s[::-1]:
            if table[i] < table[p]:
                res = res - table[i]
            else:
                res = res + table[i]
            p = i
        return res
