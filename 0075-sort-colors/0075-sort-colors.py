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

        # Process elements until i crosses r, because everything before l is guaranteed to be a 0 vs. after r will be a 2, so only need to scan between l and r
        while i <= r:
            if nums[i] == 0:
                # Swap current element with left boundary
                nums[l], nums[i] = nums[i], nums[l]
                # Expand left boundary to -> (more 0s)
                l += 1
                # Move forward — we've handled this element
                i += 1
            elif nums[i] == 2:
                # Swap current element with right boundary
                nums[r], nums[i] = nums[i], nums[r]
                # Expand right boundary to <- (more 2s)
                r -= 1
                # Don't move i — the element at nums[i] is new and needs rechecking
            elif nums[i] == 1:
                # 1s don't need to be moved because the surrounding swaps sort them passively
                i += 1
                

