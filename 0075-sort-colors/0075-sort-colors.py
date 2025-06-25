class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Time: O(2n) -> Two-pass solution w/ Bucket Sort
        Space: O(1)
        """
        # # Make a count hash map
        # buckets = collections.Counter(nums)
        # start = 0

        # # Go over nums and reassign values using hash map
        # for color in range(3):
        #     for i in range(buckets[color]):
        #         nums[i + start] = color
        #         temp = i
        #     start += buckets[color]

        """
        Time: O(n) -> One-pass solution w/ partitioning
        Space: O(1)
        """
        # l = boundary for 0s (everything before l is 0)
        # r = boundary for 2s (everything after r is 2)
        # i = current index being examined
        l, r = 0, len(nums) - 1
        i = 0

        # If we find a 0 or a 2 at i, swap with left or right respectively 
        # Only increment i when you're confident you've placed a 0 or 1 in its final place
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1
                

