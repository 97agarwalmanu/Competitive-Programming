class Solution:
    def reverse(self, x: int) -> int:
        r = str(abs(x))[::-1].lstrip('0')
        
        if x == 0 or int(r) > 2**31-1:
            return 0
        
        return r if x > 0 else '-' + r
        