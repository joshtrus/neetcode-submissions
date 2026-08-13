class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
                while left > -1 and right < len(s) and s[left] == s[right]:
                        left -=1
                        right +=1
                    
                return (s[left + 1: right])
        
        res = ""

        for i in range(len(s)):
            substring = expand(i,i)
            if len(substring) > len(res):
                res = substring
        
        for i in range(len(s) -1):
            substring = expand(i,i+1)
            if len(substring) > len(res):
                res = substring
        
        return res
            

            




        