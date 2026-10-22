class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 0:
            return 0
        # nums.sort()
        # streak = 1
        # max_streak = 1

        # for i in range(len(nums)-1):
        #     con = nums[i+1] - nums[i]
        #     if con == 1:
        #         streak += 1
        #         max_streak = max(max_streak, streak)
        #     elif con > 1:
        #         streak = 1
        # return max_streak

        hash_set = set(nums)
        max_streak = 0
        for num in hash_set:
            if num - 1 not in hash_set:
                current = num
                streak = 1
                while current+1 in hash_set:
                    streak += 1
                    current += 1

                max_streak = max(max_streak, streak)

        return max_streak


            
