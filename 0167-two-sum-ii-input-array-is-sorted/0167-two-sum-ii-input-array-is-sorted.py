class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        """
        curr_sum = numbers[0] + numbers[-1]
        left = 0
        right = len(numbers) - 1

        while left < right:
            # if curr_sum > target: need to make curr_sum smaller by decreasing right pointer
            if curr_sum > target:
                curr_sum -= numbers[right]
                right -= 1
                curr_sum += numbers[right] 
            # if curr_sum < target: need to make curr_sum bigger by increasing left pointer
            elif curr_sum < target:
                curr_sum -= numbers[left]
                left += 1
                curr_sum += numbers[left]
            # else, they must be equal: return the indices (1 indexed)
            else:
                return [(left + 1), (right + 1)]