class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_length = len(s1)
        frequency_s1 = {}
        left = 0
        right = window_length 

        for i in range(0,len(s1)):
            frequency_s1[s1[i]] = frequency_s1.get(s1[i], 0) + 1           

        while left <= len(s2)-window_length:
            freq_window = {}
            for i in range(left,right):
                freq_window[s2[i]] = freq_window.get(s2[i], 0) + 1
            if frequency_s1 == freq_window:
                return True 
            else:
                left +=1 
                right +=1 

        return False
