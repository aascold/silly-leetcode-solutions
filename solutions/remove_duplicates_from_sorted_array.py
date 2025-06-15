'''
    My solution for "Remove Duplicates from Sorted Array" problem
    https://leetcode.com/problems/remove-duplicates-from-sorted-array
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_num = None
        i = 0
        while i < len(nums):
            if not last_num is None and nums[i] == last_num:
                nums.pop(i)
            else:
                last_num = nums[i]
                i += 1
        return len(nums)