from typing import List

# is overlapping
# merge two if overlap

class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:      
        if len(intervals) < 2:
            return intervals
        elif len(intervals) == 2:
            if self.is_overlap(intervals[0], intervals[1]):
                return self.merge_2_interval(intervals[0], intervals[1])
            else:
                return intervals
        else:
            final_list = []
            intervals_tmp = self.merge(intervals[:-1]) + [intervals[-1]]
            interval_ref = intervals[-1]
            for i in range(0, len(intervals_tmp)-1):
                if self.is_overlap(interval_ref, intervals_tmp[i]):
                    interval_ref = self.merge_2_interval(interval_ref, intervals_tmp[i])[0]
                else:
                    final_list.append(intervals_tmp[i])
            final_list += [interval_ref]
            return final_list

    def is_overlap(self, int1, int2):
        if int1[0] < int2[0]:
            l, r = int1, int2
        else:
            l, r = int2, int1
        return l[1] >= r[0]
    
    def merge_2_interval(self, int1, int2):
        minv = min(int1[0], int2[0])
        maxv = max(int1[1], int2[1])
        return [[minv, maxv]]


class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        intervals.sort(key=lambda x: x[0])
        final_list = []
        interval_ref = intervals[0]
        for i in range(1, len(intervals)):
            if self.is_overlap(interval_ref, intervals[i]):
                interval_ref = self.merge_2_interval(interval_ref, intervals[i])[0]
            else:
                final_list.append(interval_ref)
                interval_ref = intervals[i]
        final_list.append(interval_ref)
        return final_list

    def bubble_sort(self, intervals):
        for i in range(len(intervals)-1):
            for j in range(len(intervals)-i-1):
                if intervals[j][0] > intervals[j+1][0]:
                    intervals[j], intervals[j+1] = intervals[j+1], intervals[j]
        return intervals

    def is_overlap(self, int1, int2):
        if int1[0] < int2[0]:
            l, r = int1, int2
        else:
            l, r = int2, int1
        return l[1] >= r[0]
    
    def merge_2_interval(self, int1, int2):
        minv = min(int1[0], int2[0])
        maxv = max(int1[1], int2[1])
        return [[minv, maxv]]


if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution2()
    print(sol.is_overlap([1, 4], [0, 2]))
    print(sol.merge_2_interval([1, 4], [0, 2]))
    print(sol.merge(intervals))