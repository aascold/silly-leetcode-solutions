'''
    My silly solution for "Longest Common Prefix" problem
    https://leetcode.com/problems/longest-common-prefix/
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]
        for s in strs:
            tmp_prefix = ''
            for i in range(min(len(longest_prefix), len(s))):
                if longest_prefix[i] == s[i]:
                    tmp_prefix += longest_prefix[i]
                else:
                    break
            longest_prefix = tmp_prefix
        return longest_prefix