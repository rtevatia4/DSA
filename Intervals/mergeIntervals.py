"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""






""" Using Graph connected components but complexity is O(n^2)
import collections


class Solution:
    def merge(self, intervals):
        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            x,y = intervals[i][0],intervals[i][1]
            right=i+1
            while right<len(intervals):
                x1,y1 = intervals[right][0],intervals[right][1]
                if x<=y1 and x1<=y:
                    graph[(x,y)].append([x1,y1])
                    graph[(x1,y1)].append([x,y])
                right+=1
        # print(graph)
        comp_nodes = collections.defaultdict(list)
        visited = set()
        component = 0
        def dfs(points,comp):
            visited.add((points[0],points[1]))
            comp_nodes[comp].append(points)
            for nei in graph[(points[0],points[1])]:
                if (nei[0],nei[1]) not in visited:
                    dfs(nei,comp)

        for interval in intervals:
            if ((interval[0],interval[1])) not in visited:
                component += 1
                dfs(interval, component)
        print(comp_nodes)
        res = []
        for comp in comp_nodes.values():
            start = min(node[0] for node in comp)
            end = max(node[1] for node in comp)
            res.append([start,end])
        return res
"""
        