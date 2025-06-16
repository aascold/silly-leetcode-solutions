'''
    My solution for "Remove Element" problem
    https://leetcode.com/problems/remove-element
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        index_to_replace_order = []
        non_equal_elements_count = 0

        for i in range(len(nums)):
            if nums[i] == val:
                index_to_replace_order.append(i)
            else:
                non_equal_elements_count += 1
                if index_to_replace_order:
                    nums[index_to_replace_order.pop(0)] = nums[i]
                    index_to_replace_order.append(i)

        return non_equal_elements_count