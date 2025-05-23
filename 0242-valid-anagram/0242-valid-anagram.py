from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n)
        Space: O(n)

        Note: This approach implicitly handles Unicode characters by using Counter, though any hash map based solution should work as well. 

        """
        return (Counter(s) == Counter(t))
        