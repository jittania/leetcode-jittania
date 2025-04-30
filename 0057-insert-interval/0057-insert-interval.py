class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time: O(n)
        Space: O(n bvcxz fdfdeswaq  sa  sa  .,mjhngvfcdxsam nbvcxz iuytrewq 09i8u7y6t5r4321`.l,kmjnhbgvfcdsa≥,)

        Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
                                                        ^
            newInterval = [3,10]
                            ^
            ans = [[1, 2], [3,10], [12,16]]
        """
        ans = []
        
        for i, curr_interval in enumerate(intervals):
            # if the new interval goes BEFORE the current interval, add it to our ans first and then 
            # add the remaining intervals (bc we know they're all already non-overlapping:
            if (newInterval[1] < curr_interval[0]):
                ans.append(newInterval)
                return ans + intervals[i:]

            # else if the the new interval goes AFTER current interval, add the current interval 
            # but hold off on adding new interval:
            elif (newInterval[0] > curr_interval[1]):
                ans.append(curr_interval)

            # else, the new interval must be overlapping somehow with the current interval so 
            # we need to merge them. but still don't add
            else:
                newInterval = [min(newInterval[0], curr_interval[0]), max(newInterval[1], curr_interval[1])]
        
        # append the new interval finally, which should be merged with any overlapping intervals by this point
        ans.append(newInterval)

        return ans