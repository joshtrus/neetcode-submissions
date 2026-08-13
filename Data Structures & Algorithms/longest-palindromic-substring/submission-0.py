class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
                while left > -1 and right < len(s) and s[left] == s[right]:
                        left -=1
                        right +=1
                    
                return (s[left + 1: right])
        
        res = {}

        for i in range(len(s)):
            substring = expand(i,i)
            res[len(substring)] = substring
        
        for i in range(len(s) -1):
            substring = expand(i,i + 1)
            res[len(substring)] = substring

        best_len = max(res.keys())
        return res[best_len]
            

            




        