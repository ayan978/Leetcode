class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1 = str(x)
        i = 0
        j = len(x1) - 1
        flag = True
        while i < j:
            if x1[i] == x1[j]:
                i += 1
                j -= 1

            else:
                flag = False
                break

        return flag
