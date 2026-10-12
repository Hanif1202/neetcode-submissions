class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # tc - o(n^2)
        # sc - o(n)
        # hash_map = set()

        # for i in range(len(nums)):
        #     if target - nums[i] in hash_map:
        #         return [nums.index(target - nums[i]),i]
        #     else:
        #         hash_map.add(nums[i])

        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
