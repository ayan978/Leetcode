class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a, b, max_len = 0, 0, 0
        s1 = set()
        while b < len(s):
            if s1.__contains__(s[b]):
                s1.discard(s[a])
                a += 1
            else:
                s1.add(s[b])
                max_len = max(len(s1), max_len)
                b += 1

        return max_len

