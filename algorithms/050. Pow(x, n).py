# Implement pow(x, n).


class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0

        x = 1 / x if n < 0 else x
        n = abs(n)
        m = 1

        while n > 1:
            if n % 2:
                m *= x
            x *= x
            n /= 2
        return m * x
