class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time: O(n)
        Space: O(1)

        Input: s = "A man, a plan, a canal: Panama"
                              ^
                                         ^

        """
        l, r = 0, len(s) - 1

        while l < r:
            # skip chars on left until an alphanum char is found
            while l < r and not s[l].isalnum():
                l += 1
            # skip chars on right until an alphanum char is found
            while l < r and not s[r].isalnum():
                r -= 1
            # if lowercase versions of letters are NOT equal, don't need to check further: can't be a palindrome
            if s[l].lower() != s[r].lower():
                return False
            # if lowercase versions of letters are equal, move both pointers inward
            l += 1
            r -= 1

        return True
