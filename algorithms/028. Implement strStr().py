# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1
# if needle is not part of haystack.


class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # cheating solution
        # return haystack.find(needle)

        # normal solution
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(i, len(needle) + i):
                if haystack[j] == needle[j - i]:
                    continue
                else:
                    break
            else:
                return i
        return -1
