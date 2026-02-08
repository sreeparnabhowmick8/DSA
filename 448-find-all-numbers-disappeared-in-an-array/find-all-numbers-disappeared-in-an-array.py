class Solution:
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
        dic={}
        res=[]
        n=len(arr)
        for i in arr:
            dic[i]=dic.get(i,0)+1
        for i in range(1,n+1):
            if i not in dic.keys():
                res.append(i) 
        return res          






        