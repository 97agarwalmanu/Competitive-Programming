class Solution:
    def binaryGap(self, N: int) -> int:
        l = list(bin(N))[2:]
        index = -1
        dist = 0
        for i,v in enumerate(l):
            if v == '1':
                if index != -1:
                    dist = max(dist, i-index)
                index = i
        return dist