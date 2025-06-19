'''
    My solution for "Search Insert Position" problem
    https://leetcode.com/problems/search-insert-position/
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while r - l > 1:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid
        if nums[r] < target:
            return r + 1
        if nums[l] < target:
            return l + 1
        return l