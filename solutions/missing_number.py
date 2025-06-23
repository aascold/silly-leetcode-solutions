'''
    Solution for "Missing Number" problem
    https://leetcode.com/problems/missing-number
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        for num in nums:
            s += num
        return int(((len(nums) + 1) * len(nums) / 2) - s)