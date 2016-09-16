# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].


class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex):
            temp = [1]
            temp.extend([sum(p) for p in zip(res, res[1:])])
            temp.append(1)
            res[:] = temp
        return res
