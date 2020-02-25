class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        steps_count = 0
        for i in range(len(points)-1):
            x_dist = abs(points[i][0] - points[i+1][0])
            y_dist = abs(points[i][1] - points[i+1][1])
            steps_count += max(x_dist, y_dist)
        return steps_count    
        