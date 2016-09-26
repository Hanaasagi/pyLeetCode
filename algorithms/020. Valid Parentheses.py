# Given a string containing just the characters '(', ')', '{', '}', '['
# and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all
# valid but "(]" and "([)]" are not.


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in dic.keys():
                if len(stack) <= 0 or dic[c] != stack.pop():
                    return False
            elif c in dic.values():
                stack.append(c)
        return len(stack) == 0
