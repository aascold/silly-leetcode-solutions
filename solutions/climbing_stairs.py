'''
    Solution for "Climbing Stairs" problem
    https://leetcode.com/problems/climbing-stairs
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0, 1, 2]
        if n < len(steps):
            return steps[n]
        for i in range(3, n + 1):
            steps.append(steps[i - 1] + steps[i - 2])
        return steps[n]