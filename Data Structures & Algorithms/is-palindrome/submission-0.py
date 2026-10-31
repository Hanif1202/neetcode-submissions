class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        
        result = ''.join(char.lower() for char in s if char.isalnum())
        right = len(result)-1

        while left < right:
            print(result[left],result[right])
            if result[left] == result[right]:
                left +=1
                right -=1
            else:
                return False
            
        return True       