import numpy as np;
class Solution:
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]]
        for start,end in intervals:
            if start<=answer[-1][1]:
                answer[-1][1]=max(answer[-1][1],end)
            else:
                    answer.append([start, end])
        return answer
