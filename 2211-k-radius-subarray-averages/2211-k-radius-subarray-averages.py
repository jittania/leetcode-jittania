class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        """
        
        Input: nums = [7,4,3,9,1,8,5,2], k = 3
                      
                                     ^
        window_size: 5
        curr_window_sum: 39

        avgs: [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        
        """
        if k == 0:
            return nums
        
        avgs = [-1] * len(nums)
        window_size = 2 * k + 1
        
        if window_size > len(nums):
            return avgs
        
        # get the sum of the first window
        curr_window_sum = sum(nums[:window_size])
        
        # use that sum to set the corresponding k-radius average in avgs using int division
        avgs[k] = curr_window_sum // window_size
        
        # now iterate over remaining nums (this is where it becomes a typical sliding window prob):
        for i in range(window_size, len(nums)):
            # add from right, remove from left
            curr_window_sum = curr_window_sum + nums[i] - nums[i - window_size]

            # update avgs
            avgs[i - k] = curr_window_sum // window_size
            
        return avgs
        
        
        
        
        
        
                
        
        