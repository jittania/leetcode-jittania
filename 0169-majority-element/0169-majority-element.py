class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Note: this is my favorite Leetcode problem of all time
        """
        Time: O(n)
        Space: O(n)
        """
        # seen = {}
        # for num in nums:
        #     if num not in seen:
        #         seen[num] = 1
        #     elif num in seen:
        #         seen[num] += 1
        #     if seen[num] > (len(nums) // 2):
        #         return num
        """
        Time: O(n)
        Space: O(1)
        Note that this solution just utilizes the Boyer-Moore voting algorithm
        """
        maj = 0
        count = 0

        for num in nums:
            if count == 0:
                maj = num
            count += (1 if num == maj else -1)
        return maj



        
        