class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # indices = {} O(nlogn) solution
        # for idx, num in enumerate(sorted(nums)):
        #     indices.setdefault(num, idx)
        # return [indices[num] for num in nums]
        
        #O(n)-> Time complexity ,O(1)-> Space Complexity
        count = [0]*102 
        for num in nums:
            count[num+1] += 1
        for i in range(1,102):
            count[i] += count[i-1]
        return [count[num] for num in nums]