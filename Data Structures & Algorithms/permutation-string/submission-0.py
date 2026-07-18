class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map1 = {}
        freq_map2 = {}
        left = 0
        for c in s1:
            freq_map1[c] = freq_map1.get(c, 0) + 1
        
        for right in range(len(s2)):
            freq_map2[s2[right]] = freq_map2.get(s2[right], 0) + 1

            while right - left + 1 > len(s1):
                freq_map2[s2[left]] -= 1
                if freq_map2[s2[left]] == 0:
                    del freq_map2[s2[left]]
                left += 1
            
            if freq_map1 == freq_map2:
                return True
        
        return False
            







        