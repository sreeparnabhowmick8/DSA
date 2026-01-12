import math
class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        arr.sort()
        n=len(arr)
        if(n==1):
            return arr[0]
        res,max1=-1,-1
        ele,count=0,0
        for i in arr:
            if i!=res:
                count=1
                res=i
            else:
                count+=1
                if(count>=max1):
                    ele=i 
                max1=max(count,max1)
        return ele   
                       
             


        