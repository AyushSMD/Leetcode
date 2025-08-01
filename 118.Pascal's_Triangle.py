class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        PascalTriangle = []
        for i in range(numRows):
            PascalTriangle.append([1])
            for j in range(1,i):
                PascalTriangle[i].append(PascalTriangle[i-1][j-1]+(PascalTriangle[i-1][j]))
            if i>0:
                PascalTriangle[i].append(1)


        return PascalTriangle

sol = Solution()
print(sol.generate(5))
        