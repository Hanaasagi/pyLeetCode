# Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

#     The length of both num1 and num2 is < 5100.
#     Both num1 and num2 contains only digits 0-9.
#     Both num1 and num2 does not contain any leading zero.
#     You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution(object):

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = 0
        res = []
        carry = 0
        len1 = len(num1)
        len2 = len(num2)
        length = max(len1, len2)
        while i < length:
            val1 = num1[len1 - i - 1] if len1 - i - 1 >= 0 else '0'
            val2 = num2[len2 - i - 1] if len2 - i - 1 >= 0 else '0'
            val = ord(val1) + ord(val2) + carry - 96
            if val > 9:
                carry = val / 10
                val = val % 10
            else:
                carry = 0
            res.insert(0, chr(val + 48))
            i += 1
        if carry != 0:
            res.insert(0, chr(carry + 48))
        return ''.join(res)
