class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic={}
        res=[]
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for i in dic:
            if dic[i]==2:
                res.append(i) 
        return res            
        