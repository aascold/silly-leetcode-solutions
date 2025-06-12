'''
    My silly solution for "Valid Parentheses" problem
    https://leetcode.com/problems/valid-parentheses
'''

class Solution:
    def isValid(self, s: str) -> bool:
        close_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        brackets_stack = []
        for ch in s:
            if ch in close_brackets:
                if not brackets_stack or close_brackets[ch] != brackets_stack[-1]:
                    return False
                else:
                    brackets_stack.pop()
            else:
                brackets_stack.append(ch)
        
        return brackets_stack == []
