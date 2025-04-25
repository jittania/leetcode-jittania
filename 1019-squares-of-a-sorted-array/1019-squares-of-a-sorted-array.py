class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [-7,-3,2,3,11]
                             ^
                             ^
                        49,9,4,9,121
        Output: [4,9,9,49,121]
        """
        left = 0
        right = len(nums) - 1
        
        # create an empty arr of length(nums)
        squares = [0] * len(nums)
        
        # compare squared values at left and right indices: add largest to end of new array
        for i in range(len(nums) - 1, -1, -1):
            if (nums[left] ** 2) > (nums[right] ** 2):
                squares[i] = nums[left] ** 2
                left += 1
            else:
                squares[i] = nums[right] ** 2
                right -= 1

        return squares
        