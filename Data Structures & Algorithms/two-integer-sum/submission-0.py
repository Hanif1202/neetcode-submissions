class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = set()

        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [nums.index(target - nums[i]),i]
            else:
                hash_map.add(nums[i])
