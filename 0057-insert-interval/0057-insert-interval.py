class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Time: O(n)
        Space: O(n)
        """
        mod_intervals = []

        for curr_i, curr_interval in enumerate(intervals):
            # There are only 3 ways to handle new_interval depending on how it relates to curr_interval:
            # 1. new_interval should come before the current interval
                # insert new_interval before and append remaining intervals (we are done)
            if new_interval[1] < curr_interval[0]:
                mod_intervals.append(new_interval)
                return mod_intervals + intervals[curr_i:]
            # 2. new_interval should come after the current interval, but could overlap with the next interval
                # append current interval only to our answer, leave new_interval alone
            elif new_interval[0] > curr_interval[1]:
                mod_intervals.append(curr_interval)
            # 3. new_interval overlaps somehow with the current interval
                # merge current interval into new_interval, but don't append to our answer
            else:
                new_interval = [min(curr_interval[0], new_interval[0]), max(curr_interval[1], new_interval[1])]

        # since we're at the end of intervals and haven't added new_interval yet, add it now
        mod_intervals.append(new_interval)

        return mod_intervals