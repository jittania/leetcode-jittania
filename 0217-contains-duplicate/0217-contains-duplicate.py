class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        Note that by sorting the input first then checking for duplicate neighbors we could eliminate the need for a hash set and achieve O(1) space at cost of increasing time to O(n log n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False