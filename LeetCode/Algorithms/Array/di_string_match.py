class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        A = [i for i in range(len(S)+1)]
        arr = []
        i = 0
        j = len(S)
        for s in S:
            if s=='I': 
                arr.append(A[i])
                i += 1
            else: 
                arr.append(A[j])
                j -= 1
        arr.append(A[i])
        return arr
            
        
        