class Solution:

    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        numset = sorted(set(nums))
        longest = 0
        temp = 1
        for i, v in enumerate(numset[:-1]):
            never_ran = True
            if v == numset[i + 1] - 1:
                temp += 1
                continue
            longest = max(longest, temp)
            never_ran = False
            temp = 1
        if never_ran:
            longest = max(longest, temp)
        return longest


a = Solution()
print(a.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
