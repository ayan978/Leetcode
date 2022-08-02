class Solution(object):
    def twoSum(self, nums, target):
        l1 = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    l1.append(i)
                    l1.append(j)
                    break
        return l1
