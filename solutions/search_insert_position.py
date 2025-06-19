'''
    My solution for "Search Insert Position" problem
    https://leetcode.com/problems/search-insert-position/
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)