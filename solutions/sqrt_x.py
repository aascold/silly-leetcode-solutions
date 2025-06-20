'''
    My solution for "Sqrt(x)" problem
    https://leetcode.com/problems/sqrtx
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
        return l if l * l < x else l - 1