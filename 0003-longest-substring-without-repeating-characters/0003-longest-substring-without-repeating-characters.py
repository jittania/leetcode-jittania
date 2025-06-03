class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(n)

        Input = "tmmzuxt"
                   ^
                    ^

        seen = {t: 0, m: 1}
        max_length = 2
        """
        if len(s) <= 1:
            return len(s)
        
        left = 0
        seen = {s[left]: 1}
        max_length = 1
        
        for right in range(1, len(s)):
            if s[right] not in seen or seen[s[right]] == 0:
                seen[s[right]] = 1
                max_length = max(max_length, (right - left + 1))
            else:
                seen[s[right]] += 1
                while seen[s[right]] > 1:
                    seen[s[left]] -= 1
                    left += 1
        return max_length
            

        
        