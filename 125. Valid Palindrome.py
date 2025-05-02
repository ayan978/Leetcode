class Solution(object):
    def isPalindrome(self, s):
        s = s.strip()
        if len(s)==0:
            return True
        s = s.lower()
        s1 = s2 = ''
        itr1 = 0
        itr2 = len(s)-1
        length = len(s)

        while itr1<length or itr2>=0:
            if s[itr1].isalnum():
                s1 += s[itr1]
            if s[itr2].isalnum():
                s2 += s[itr2]
            itr1+=1
            itr2-=1

        return s1==s2

