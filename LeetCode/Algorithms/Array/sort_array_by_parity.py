class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [a for a in A if not a%2] + [a for a in A if a%2]    
        