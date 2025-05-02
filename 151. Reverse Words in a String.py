class Solution(object):
    def reverseWords(self, s):
        s1 = s.strip()
        s2 = ''
        arr1 = s1.split(' ')
        length = len(arr1)
        for i in range(length-1, -1, -1):
            if arr1[i]!='':
                s2 = s2+arr1[i]+' '
        s2 = s2.strip()
        return s2
