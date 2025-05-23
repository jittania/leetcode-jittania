from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n)
        Space: O(n)

        """
        return (Counter(s) == Counter(t))
        