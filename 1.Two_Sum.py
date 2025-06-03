class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, current_num in enumerate(nums):
            for add_to_index,comp_num in enumerate(nums[index + 1 : :]):
                if current_num+comp_num==target:
                    return [index,index+add_to_index+1]

test = Solution()

print(test.twoSum(nums = [3,3], target = 6))