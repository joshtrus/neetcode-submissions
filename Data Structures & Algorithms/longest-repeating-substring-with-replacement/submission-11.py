class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #assumptions
        #---------------------------------------
        #Intial string contains multiple characters in random order
        #I can change at most k to create a 1-char substring 
        #Change can be done anywhere in any order
        #Returning length of longest one

        #Clarifying Questions
        #---------------------------------------
        #Theres no priority in which char is replaced


        #Potential Approaches
        #---------------------------------------
        #sliding window approach
        #for loop moving right pointer
        #inner while moving left pointer
        #validity of substring is len(window) - most freq char <= k
        #Time complexity O(n) where n is the list of string
        #Space complexity is O(1)

        # Input: s = "AAABABB", k = 1


        #Better Approach
        #---------------------------------------
        char_map = {}
        left = 0
        maxSize = 0
        max_freq = 0
        if not s:
            return 0
        
        for right in range(len(s)):
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            max_freq = max(max_freq, char_map[s[right]]) 


            while (right - left + 1) - max_freq > k:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1
            
            maxSize = max(maxSize, (right - left + 1))
        
        return maxSize


            











