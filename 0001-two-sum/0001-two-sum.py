class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """

        """

        ans = []
        temp_hash = {}

        for i, num in enumerate(nums):
            if (target - num) not in temp_hash:
                temp_hash[num] = i
            else:
                return [temp_hash[target - num], i]



