class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range (len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i,hashmap[complement]]
            hashmap[nums[i]]=i
        return []
    
solobj = Solution()
print(solobj.twoSum([3,3],6))
