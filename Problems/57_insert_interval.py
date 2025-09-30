class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        i = 0
        s, e = newInterval

        # case1: s보다 먼저 끝
        while i<len(intervals) and intervals[i][1]<s:
            output.append(intervals[i])
            i += 1

        # case2: 겹치는 구간
        while i<len(intervals) and intervals[i][0]<=e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1
        output.append([s, e])

        # case3: e보다 뒤
        while i<len(intervals):
            output.append(intervals[i])
            i += 1
        
        return output
