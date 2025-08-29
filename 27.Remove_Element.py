class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        replace_index = 0
        for i,n in enumerate(nums):
            if n == val:
                replace_index += 1
            else:
                nums[i-replace_index]=n

        return replace_index,nums[:-replace_index]

sol = Solution()
print (sol.removeElement([0,1,2,2,3,0,4,2],2))