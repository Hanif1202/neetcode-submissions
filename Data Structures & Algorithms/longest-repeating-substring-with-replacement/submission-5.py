class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_freq = 0
        maximum = 0

        for right in range(len(s)):

            freq[s[right]] = freq.get(s[right], 0) + 1

            max_freq = max(max_freq, freq[s[right]])

            window_length = right - left + 1

            replacements = window_length - max_freq

            if replacements > k:
                freq[s[left]] -= 1
                left += 1

            maximum = max(maximum, right - left + 1)

        return maximum


        
        
                 