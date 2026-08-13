class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left, right):
            amount = 0
            while left > -1 and right < len(s) and s[left] == s[right]:
                amount +=1
                left  -= 1
                right += 1
            
            return amount 
        
        res = 0

        for i in range(len(s)):
            res += expand(i,i)

            res += expand(i,i + 1)
        
        return res
        
                
        