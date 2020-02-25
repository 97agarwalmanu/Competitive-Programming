class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        count = [0,0]
        for i in range(len(chips)):
            count[chips[i]%2] += 1
        return min(count)
        