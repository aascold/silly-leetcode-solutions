'''
    My solution for "Min Cost Climbing Stairs" problem
    https://leetcode.com/problems/min-cost-climbing-stairs
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCosts = []
        for i in range(len(cost) + 1):
            if i < 2:
                minCosts.append(cost[i])
            else:
                minCosts.append(min(minCosts[i - 1], minCosts[i - 2]))
                if i < len(cost):
                    minCosts[i] += cost[i]
        return minCosts[-1]