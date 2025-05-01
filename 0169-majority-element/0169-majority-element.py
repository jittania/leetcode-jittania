class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            elif num in seen:
                seen[num] += 1
            if seen[num] > (len(nums) // 2):
                return num

        
        