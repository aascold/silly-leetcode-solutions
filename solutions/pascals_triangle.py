'''
	Solution for "Pascal's Triangle" problem
	https://leetcode.com/problems/pascals-triangle
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            rows.append([1])
            for j in range(i - 1):
                rows[i].append(rows[i - 1][j] + rows[i - 1][j + 1])
            rows[i].append(1)
        return rows