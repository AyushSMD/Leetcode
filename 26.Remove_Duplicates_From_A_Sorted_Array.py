class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 0
        lowest = -101
        for num in nums:
            if num > lowest:
                nums[index]=num
                lowest = num
                index+=1
        
        return index

Solution = Solution()
print (Solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
