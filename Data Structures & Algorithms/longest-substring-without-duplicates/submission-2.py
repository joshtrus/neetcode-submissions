class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_char = set()
        max_len = 0
        i = 0

        for c in s:
            while c in unique_char:
                unique_char.remove(s[i])
                i+=1
            
            unique_char.add(c)
            max_len = max(max_len, len(unique_char))

        
        return max_len



   
   
  