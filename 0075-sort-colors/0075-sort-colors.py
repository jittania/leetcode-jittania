class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Time: O(2n) -> Two-pass solution
        Space: O(1)
        """
        # Make a count hash map (first pass)
        counts = collections.Counter(nums)
        start = 0

        # Go over nums and reassign values using hash map
        for color in range(3):
            for i in range(counts[color]):
                nums[i + start] = color
                temp = i
            start += counts[color]

        """
        Time: O(n) -> One-pass solution
        Space: O(1)
        """