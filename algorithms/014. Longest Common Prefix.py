# Write a function to find the longest common prefix string amongst an array of strings.


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for s in zip(*strs):
            if reduce(lambda x, y: y if x == y else False, s):
                res += s[0]
            else:
                break
        return res
