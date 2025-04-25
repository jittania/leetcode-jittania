class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        arr of ints (nums), int (target) --> arr of ints (indices)

        Input: nums = [3,3], target = 6
                         ^
        { 3: 0 }
                      
        Output: [0,1]

        Input: nums = [2,7,11,15], target = 9
                       ^ 
        {}
        Output: [0,1]

        - find the vals in nums that add up to target and return their positions
        - vals must be distinct (have different positions)
        - Space
        - Time
        - DRY code
        - Refactor

        """

        ans = []
        temp_hash = {}

        for i, num in enumerate(nums):
            if (target - num) not in temp_hash:
                temp_hash[num] = i
            else:
                return [temp_hash[target - num], i]



