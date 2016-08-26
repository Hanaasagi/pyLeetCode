# Given a non-negative number represented as an array of digits, plus one
# to the number.

# The digits are stored such that the most significant digit is at the
# head of the list.


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        carry = 1
        for i in reversed(digits):
            temp = (i + carry) % 10
            res.insert(0, temp)
            if temp == 0 and carry == 1:
                carry = 1
            else:
                carry = 0
        if carry:
            res.insert(0, carry)
        return res
