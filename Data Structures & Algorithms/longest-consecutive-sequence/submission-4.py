class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums.sort()
        streak = 1
        max_streak = 1

        for i in range(len(nums)-1):
            con = nums[i+1] - nums[i]
            if con == 1:
                streak += 1
                max_streak = max(max_streak, streak)
            elif con > 1:
                streak = 1
        return max_streak