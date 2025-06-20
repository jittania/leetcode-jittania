class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        singles = set()
        max_palindrome_length = 0

        for char in s:
            # if it's already in singles, we have a pair - can remove it and update counter
            if char in singles:
                max_palindrome_length += 2
                singles.discard(char) # apparently using discard doesn't raise a KeyError - doesn't matter here but still kind of a fun fact

            # else it's unpaired - add it to singles, but don't update counter
            else:
                singles.add(char)
        
        # if anything is left over in singles at the end, we can take at most one char from that
        if len(singles) > 0:
            max_palindrome_length += 1

        return max_palindrome_length
        



