class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)

        Input: nums = [1,2,3,1]


        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False