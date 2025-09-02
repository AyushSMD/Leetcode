class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] != 9:
            digits[-1]+=1
            return digits
        digits = (str)((int)("".join(map(str,digits)))+1)

        return [int(x) for x in digits]

sol = Solution()
print (sol.plusOne([9]))
        