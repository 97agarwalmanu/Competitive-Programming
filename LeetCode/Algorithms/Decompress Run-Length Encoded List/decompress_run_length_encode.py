class Solution:
    def decompressRLElist(self, nums):
        arr = []
        for i in range(0,len(nums),2):
            arr_de = [nums[i+1] for j in range(nums[i])]
            arr = arr + arr_de
        return arr