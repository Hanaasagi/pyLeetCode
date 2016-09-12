# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1], ]
        for i in range(numRows - 1):
            temp = [1]
            temp.extend([sum(p) for p in zip(res[i], res[i][1:])])
            temp.append(1)
            res.append(temp)
        return res
