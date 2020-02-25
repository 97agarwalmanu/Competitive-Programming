import math
class Solution:
    def findNumbers(self, nums) -> int:
        num_even_length = 0
        for num in nums:
            if (int(math.log10(num))+1) % 2 == 0: # Faster than 92%
            #if len(str(num)) % 2 == 0:           # Faster than 74%
            #if get_num_length(num) % 2 == 0:     # Faster than 15%
                num_even_length += 1
        return num_even_length
            
    def get_num_length(self, num: int) -> int:
        num_len = 0
        while num > 0:
            num = int(num/10)
            num_len += 1
        return num_len