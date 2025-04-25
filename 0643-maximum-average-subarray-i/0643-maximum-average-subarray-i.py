class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        nums = [1,12,-5,-6,50,3], k = 4
                      ^
                                ^
        curr_sum = 42
        max_sum = 51
        
        """
        
        # Get subarray with largest sum and return sum / k
        left = 0
        curr_sum = max_sum = sum(nums[:k])
        
        for right in range(k, len(nums)):
            curr_sum += nums[right]
            curr_sum -= nums[left]
            max_sum = max(curr_sum, max_sum)
            left += 1
            
        return max_sum / k
            
            
            
        
        