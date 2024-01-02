class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low, high = 0, len(nums) - 1

        while(low<=high):
            if nums[low] == target:
                return low
            elif nums[high] == target:
                return high
            low += 1
            high -= 1
            
        return -1
