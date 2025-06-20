class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Time:
        Space:

        Input: s = "abccccdd"
                           ^
        
        singles = (a, b)
        max_palindrome_length = 7

        """
        singles = set()
        max_palindrome_length = 0

        for char in s:
            # if it's already in singles, we have a pair - can remove it and update counter
            if char in singles:
                max_palindrome_length += 2
                singles.discard(char)

            # else it's unpaired - add it to singles, but don't update counter
            else:
                singles.add(char)
        
        # if anything is left over in singles at the end, we can take at most one char from that
        if len(singles) > 0:
            max_palindrome_length += 1

        return max_palindrome_length
        



