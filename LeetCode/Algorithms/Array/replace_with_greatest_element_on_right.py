class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        me,arr[-1] = arr[-1],-1
        
        for i in range(len(arr)-2,-1,-1):
            arr[i],me = me,max(me,arr[i])
            
        return arr
        