'''
    My silly solution for "Roman to Integer" problem
    https://leetcode.com/problems/roman-to-integer
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        dec_int = 0
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        prev_digit = None
        for digit in s:
            if prev_digit and roman[digit] > roman[prev_digit]:
                dec_int += roman[digit] - roman[prev_digit] * 2
            else:
                dec_int += roman[digit]
            prev_digit = digit
        return dec_int