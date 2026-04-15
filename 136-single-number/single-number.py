class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        dic={}
        for i in arr:
            dic[i]=dic.get(i,0)+1
        for i in arr:
            if(dic[i]==1):
                return i           
            
        