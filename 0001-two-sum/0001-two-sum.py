class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n)

        Input: nums = [3,3], target = 6
                         ^
        seen = {3:0}
        """
        seen = {}

        for index, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target - num], index]
            else:
                seen[num] = index

        