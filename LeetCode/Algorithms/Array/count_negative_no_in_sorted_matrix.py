class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            count += self.lower_bound_binary_search(row)
        return(count)
    
    def lower_bound_binary_search(self, row: List[int]) -> int:
        start, end = 0, len(row)
        while start<end:
            mid = start +(end -start) // 2
            if row[mid]<0:
                end = mid
            else:
                start = mid+1
        return len(row)- start
        