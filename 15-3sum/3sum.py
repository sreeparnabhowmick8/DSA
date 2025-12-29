
from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # nums.sort()
        # l= set()
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             s=nums[i]
        #             p=nums[j]
        #             n=nums[k]
        #             if(s+p+n==0):
        #                 l.add((s,p,n))
        # return list(l)
        res=[]
        nums.sort()
        for i ,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                threesum=a+nums[l]+nums[r]
                if(threesum>0):
                    r-=1
                elif(threesum<0):
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res                                                       
                        
                                       
                    

        