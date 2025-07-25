'''
    Solution for "Count Complete Tree Nodes" problem
    https://leetcode.com/problems/count-complete-tree-nodes
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)

        if left_depth == right_depth:
            return 2 ** left_depth + self.countNodes(root.right)
        else:
            return 2 ** right_depth + self.countNodes(root.left)
        
    def getDepth(self, node: Optional[TreeNode]) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth
