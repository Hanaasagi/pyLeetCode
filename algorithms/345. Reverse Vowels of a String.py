# Write a function that takes a string as input and reverse only the
# vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".


class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = ['a', 'e', 'i', 'o', 'u']
        vowel.extend(''.join(vowel).upper())
        ptr1 = 0
        ptr2 = len(s) - 1
        l = list(s)
        while ptr1 < ptr2:
            if l[ptr1] not in vowel:
                ptr1 += 1
            if l[ptr2] not in vowel:
                ptr2 -= 1
            if l[ptr1] in vowel and l[ptr2] in vowel:
                l[ptr1], l[ptr2] = l[ptr2], l[ptr1]
                ptr1 += 1
                ptr2 -= 1
        return ''.join(l)
