class Solution:        
    def searchInsert(self, nums: list[int], target: int) -> int:
        print(nums)
        if target == nums[len(nums)//2]:
            return len(nums)//2
        if target<nums[0]:
            return 0
        if target>nums[len(nums)-1]:
            return len(nums)
        if nums[len(nums)//2-1]<target < nums[len(nums)//2]:
            return len(nums)//2
        elif nums[len(nums)//2-1]<target > nums[len(nums)//2]:
            return self.searchInsert(nums[(len(nums)//2):],target) + len(nums)//2
        else:
            return self.searchInsert(nums[:(len(nums)//2)],target)
    
sol = Solution()
print (sol.searchInsert(nums = [1,3,5], target = 4))
        