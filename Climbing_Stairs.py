class Solution(object):
    def climbStairs(self, n):
        
        first, second = 1, 1
        result = None
        for i in range(n - 1):
            temp = second
            second = first + second
            first = temp

        return second
