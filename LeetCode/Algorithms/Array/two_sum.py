class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if nums[i] not in hashed:
                hashed[pair]=i
            else:
                return hashed[nums[i]],i