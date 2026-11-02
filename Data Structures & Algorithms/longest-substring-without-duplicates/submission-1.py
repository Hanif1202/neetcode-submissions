class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        contiguous = 0

        seen = {}

        while right < len(s):
            current_max = 0
            if  s[right] in seen:
                left = max(left, seen[s[right]] + 1)
                seen[s[right]] = right
                current_max = right - left + 1
                contiguous = max(contiguous , current_max)
                right +=1
                
            else:
                seen[s[right]] = right
                current_max = right - left + 1
                contiguous = max(contiguous , current_max)
                right +=1
                

        return contiguous

                

        
        