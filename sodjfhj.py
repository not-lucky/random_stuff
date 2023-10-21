class Solution:

    def findMedianSortedArrays(self, nums1: list[int],
                               nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        n = len(nums1)
        if n % 2 == 0:
            return (nums1[n // 2] + nums1[n // 2 -1]) / 2
        else:
            return nums1[n // 2]


a = Solution()
print(a.findMedianSortedArrays([1, 3], [2]))
