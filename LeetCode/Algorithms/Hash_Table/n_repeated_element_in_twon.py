class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dic = {}
        for val in A:
            if dic.get(val) == None:
                dic[val] = 1
            else:
                return val