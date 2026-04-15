class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        res=0
        for i in arr:
            res^=i
        return res               
            
        