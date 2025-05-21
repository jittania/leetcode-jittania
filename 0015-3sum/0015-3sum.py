class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time:
        Space:

        Input: [-3, 3, 4, -3, 1, 2]

        [-3, -3, 1, 2, 3, 4]

        """
        ans = []

        # Sort the input array
        nums.sort()
        
        # Handle dups by using each num in input array as a 
        # possible first value, where a + b + c = 0
        for index, a in enumerate(nums):
            # if `a`` isn't the first value in the input array, and 
            # it's the same value as the last `a`` we checked, skip this one
            if index > 0 and (a == nums[index - 1]):
                continue

            # Do two sum with l and r pointers on remaining subarray
            # to get our `b` and `c` values
            left, right = index + 1, len(nums) - 1
            while left < right:
                curr_sum = a + nums[left] + nums[right]
                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    ans.append([a, nums[left], nums[right]])
                    # updating pointers in this else case is kind of wild,
                    # but we must do it:
                    left += 1
                    # this skips over any duplicates of nums[left]:
                    while (nums[left] == nums[left - 1]) and left < right:
                        left += 1

        return ans