class Solution:
    def climbStairs(self, n: int) -> int:
        stair_ways = [1,2]
        for ways in range(2,n):
            stair_ways.append(stair_ways[ways-1]+stair_ways[ways-2])

        return stair_ways[n-1]

sol = Solution()
print (sol.climbStairs(1))