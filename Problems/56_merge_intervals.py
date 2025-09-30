class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: x[0])
        i = 0

        while i < len(intervals):
            s, e = intervals[i]
            i += 1
            while i < len(intervals) and e >= intervals[i][0]:
                s = min(s, intervals[i][0])
                e = max(e, intervals[i][1])
                i += 1
            output.append([s, e])

        return output
