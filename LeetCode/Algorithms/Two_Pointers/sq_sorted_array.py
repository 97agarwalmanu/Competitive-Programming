class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        start, end = 0, n-1
        sq = [0]*n
        for i in range(n-1,-1,-1):
            if abs(A[start]) > abs(A[end]):
                sq[i] = A[start]*A[start]
                start += 1
            else:
                sq[i] = A[end]*A[end]
                end -= 1
        return sq
                