# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        table = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                 (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                 (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        result = ''
        while len(table) > 0:
            (val, roman) = table[0]
            if num < val:
                table.pop(0)
            else:
                num -= val
                result += roman
        return result
