class Solution:
    def reverse(self, x: int) -> int:
        s = 1
        if x < 0:
            x = x*-1
            s = -1
        
        x = str(x)

        x = int(x[::-1]) * s

        if not -2147483648 <= x <= 2147483647:
            return 0

        return x

sol = Solution()
print(sol.reverse(-123))




# 7. Reverse Integer
# Medium
# Topics
# premium lock icon
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21