class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # if len(s1) > len(s2):
        #     return False

        # window_length = len(s1)
        # frequency_s1 = {}
        # left = 0
        # right = window_length 

        # for i in range(0,len(s1)):
        #     frequency_s1[s1[i]] = frequency_s1.get(s1[i], 0) + 1           

        # while left <= len(s2)-window_length:
        #     freq_window = {}
        #     for i in range(left,right):
        #         freq_window[s2[i]] = freq_window.get(s2[i], 0) + 1
        #     if frequency_s1 == freq_window:
        #         return True 
        #     else:
        #         left +=1 
        #         right +=1 

        # return False
        import string
        alphabet_dict = {letter: 0 for letter in string.ascii_lowercase}
        left = 0
        right = len(s1)
        
        for s in s1:
            alphabet_dict[s] =alphabet_dict[s] +1
        
        for s in s2[:len(s1)]:
            alphabet_dict[s] =alphabet_dict[s] -1
        
        while right < len(s2):
            if all(v == 0 for v in alphabet_dict.values()):
                return True
            alphabet_dict[s2[left]] = alphabet_dict[s2[left]] +1
            alphabet_dict[s2[right]] = alphabet_dict[s2[right]] -1
            left +=1
            right +=1
        return all(v == 0 for v in alphabet_dict.values())