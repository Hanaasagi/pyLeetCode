# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".


class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ['' for i in range(max(len(a), len(b)) + 1)]
        carry = 0
        a_len = len(a)
        b_len = len(b)
        for i in range(len(res)):
            p1 = int(a[a_len - i - 1]) if i < a_len else 0
            p2 = int(b[b_len - i - 1]) if i < b_len else 0
            s = p1 + p2 + carry
            res[len(res) - 1 - i] = str(s % 2)
            carry = s / 2
        if res[0] == '0':
            return ''.join(res[1:])
        else:
            return ''.join(res)
