import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            index1 = int(math.floor((len(nums1) - 1) / 2))
            index2 = int(math.ceil((len(nums1) - 1) / 2))

            median = (nums1[index1] + nums1[index2]) / 2

        else:
            index = int(len(nums1) - 1) // 2
            median = nums1[index]

        return median

s = Solution()
print(s.findMedianSortedArrays([1,3],[2]))
print(s.findMedianSortedArrays([1,2],[3,4]))