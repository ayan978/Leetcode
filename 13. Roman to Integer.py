class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0

        for i in range(len(s)):
            if i < (len(s) - 1) and dict1[s[i]] < dict1[s[i + 1]]:
                num -= dict1[s[i]]
            else:
                num += dict1[s[i]]

        return num