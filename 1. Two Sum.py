class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        length = len(nums)

        for i in range(length):
            difference = target - nums[i]
            if difference in dict1:
                return [dict1[difference], i]
            dict1[nums[i]] = i
