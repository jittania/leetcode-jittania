class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            # if curr_sum > target: need to make curr_sum smaller by decreasing right pointer
            if curr_sum > target:
                right -= 1
            # if curr_sum < target: need to make curr_sum bigger by increasing left pointer
            elif curr_sum < target:
                left += 1
            # else, they must be equal: return the indices (1 indexed)
            else:
                return [(left + 1), (right + 1)]