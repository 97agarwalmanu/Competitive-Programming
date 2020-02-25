class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[y^1 for y in i] for i in [reversed(x) for x in A]]        